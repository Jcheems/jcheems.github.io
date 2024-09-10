wind_active = False  # Select whether you want to activate wind or not
group_number = 22  # Enter your group number here

'''
mass:  1.2665675038538184 
rotational_inertia:  0.2850921475190987 
drag_coefficient:  0.26180807356941277 
reference_area:  0.14986306536729144 
thrust_coefficient:  1.984e-07 
rotor_time_constant:  0.059212682285142655 
rotor_constant:  6432 
omega_b:  1779
'''
# Physical constants
g = 9.81             # Gravitational acceleration (m/s^2)
m = 1.2665675038538184               # Mass of the drone (kg)
Ixx = 0.2850921475190987         # Mass moment of inertia around the x-axis (kg*m^2)
L = 0.14986306536729144              # Distance between the drone's rotors (m)

# Integral control accumulators for error integration
e_int_y = 0          # Integral of the y-axis position error
e_int_x = 0          # Integral of the x-axis position error
e_int_phi = 0        # Integral of the orientation error (phi)

# Initialise the perturbation to 0
estimated_disturbance_y = 0
estimated_disturbance_x = 0

def update_disturbance_observer(vx, vy, control_input_x, control_input_y, dt):
    """
    Updates estimates of external disturbances affecting the drone along the x and y axes.
    The function adjusts disturbance estimates based on current velocities and control inputs, employing a linear blend to smooth changes over time.

    Args:
        vx (float): Current velocity of the drone along the x-axis.
        vy (float): Current velocity of the drone along the y-axis.
        control_input_x (float): Control force along the x-axis.
        control_input_y (float): Control force along the y-axis.
        dt (float): Time step for the update. Currently unused, reserved for future use.

    Returns:
        tuple: Updated disturbance estimates along the x and y axes.

    Notes:
        - Alpha and beta are tuning parameters that determine the sensitivity of the observer to changes in velocity and control input.
        - Adjust these parameters to balance responsiveness and stability.
    """
    global estimated_disturbance_x, estimated_disturbance_y
    # Observer model parameters
    alpha = 0.3 # x-axis perturbation parameter
    beta = 0.2 # y-axis perturbation parameter

    # Updating perturbation estimates
    estimated_disturbance_x = (1 - alpha) * estimated_disturbance_x + alpha * (vx - control_input_x / m)
    estimated_disturbance_y = (1 - beta) * estimated_disturbance_y + beta * (vy - control_input_y / m)

    return estimated_disturbance_x, estimated_disturbance_y

def dynamic_pid_adjustment(err_x, err_y, vx, vy):
    """
    Dynamically adjusts PID parameters based on position error and velocity.

    Parameters:
        err_x (float): Position error along the x-axis.
        err_y (float): Position error along the y-axis.
        vx (float): Velocity along the x-axis.
        vy (float): Velocity along the y-axis.

    Returns:
        tuple: Adjusted PID parameters for x-axis (Kp_x, Kd_x, Ki_x) and y-axis (Kp_y, Kd_y, Ki_y).
    """
    # Initialise default PID parameters
    Kp_x, Kd_x, Ki_x = 1.0, 4.0, 0.1
    Kp_y, Kd_y, Ki_y = 180, 240, 20

    # Dynamic adjustment of the X-axis
    if abs(err_x) > 0.4:
        Kp_x += 0.5
        Kd_x += 1.0

    if abs(vx) > 1.0:
        Kd_x += 0.5

    # Dynamic adjustment of the Y-axis
    if abs(err_y) > 0.4:
        Kp_y += 50
        Kd_y += 100

    if abs(vy) > 1.0:
        Kd_y += 50

    return (Kp_x, Kd_x, Ki_x), (Kp_y, Kd_y, Ki_y)

# Implement a controller with attitude control
def controller(state, target_pos, dt):
    """
    Calculate the control signals for position and orientation based on PID controllers.

    Args:
    state (list): Contains the current state [x, y, vx, vy, phi, phidot]
    target_pos (list): Desired position [x_des, y_des]
    dt (float): Time step for integral calculation

    Returns:
    tuple: Control signals for the motors (u1_clamped, u2_clamped)
    """
    # Unpack current state and target position
    global e_int_y, e_int_x, e_int_phi, estimated_disturbance_x, estimated_disturbance_y
    x, y, vx, vy, phi, phidot = state
    x_des, y_des = target_pos

    # PID coefficients for x-axis control
    Kp_x = 1.0 #0.85        # Proportional gain for x
    Kd_x = 4.0 #1.75       # Derivative gain for x
    Ki_x = 0.1 #0.08        # Integral gain for x

    # PID coefficients for y-axis control
    Kp_y = 160          # Proportional gain for y
    Kd_y = 240           # Derivative gain for y
    Ki_y = 20        # Integral gain for y

    # PID coefficients for phi (orientation) control
    Kp_phi = 30 #20      # Proportional gain for phi
    Kd_phi = 20 #15      # Derivative gain for phi
    Ki_phi = 1.0 #0.5      # Integral gain for phi

    # Calculate positional errors
    err_y = y - y_des
    err_x = x - x_des

    # Dynamic adjustment of PID parameters
    (Kp_x, Kd_x, Ki_x), (Kp_y, Kd_y, Ki_y) = dynamic_pid_adjustment(err_x, err_y, vx, vy)

    # Integral separation
    if abs(err_x) < 0.4:
        e_int_x += err_x * dt
    if abs(err_y) < 0.4:
        e_int_y += err_y * dt

    # Update integral accumulators with clamping to prevent windup
    e_int_y = min(max(e_int_y + err_y * dt, -0.5), 0.5)
    e_int_x = min(max(e_int_x + err_x * dt, -0.5),0.5)


    # Calculate target orientation (phi_c) based on x-axis control
    phi_c = -1/g * (Kd_x * vx + Kp_x * err_x + Ki_x * e_int_x)
    err_phi = phi - phi_c  

    # Update integral accumulator for phi
    e_int_phi = min(max(e_int_phi + err_phi * dt, -0.2), 0.2)

    # Calculate PID-based forces and moments
    F_x = m * (Kd_x * vx + Kp_x * err_x + Ki_x * e_int_x)
    F_y = m * (g + Kd_y * vy + Kp_y * err_y + Ki_y * e_int_y)
    M = Ixx * (Kd_phi * phidot + Kp_phi * err_phi + Ki_phi * e_int_phi)

    # Update the disturbance observer
    estimated_dx, estimated_dy = update_disturbance_observer(vx, vy, F_x, F_y, dt)

    # Perturbation compensation
    F_x -= estimated_dx * m
    F_y -= estimated_dy * m

    # Calculate Motor Command
    u1 = 0.5 * (F_y - M / L)
    u2 = 0.5 * (F_y + M / L)
    u1_clamped = min(max(0, u1), 1.0)
    u2_clamped = min(max(0, u2), 1.0)

    return u1_clamped, u2_clamped
