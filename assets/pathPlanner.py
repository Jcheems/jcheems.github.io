# Import any libraries required
import random

# The main path planning function. Additional functions, classes, 
# variables, libraries, etc. can be added to the file, but this
# function must always be defined with these arguments and must 
# return an array ('list') of coordinates (col,row).
#DO NOT EDIT THIS FUNCTION DECLARATION
def do_a_star(grid, start, end, display_message):

    # Get grid dimensions
    COL = len(grid)
    ROW = len(grid[0])

    # Initialize open list, closed list and directing dictionary 
    open_list = []  # Keep track of nodes to be evaluated
    closed_list = set()  # Keep track of nodes already evaluated
    came_from = {}  # Store the path taken to reach each node

    # Initialize g score dictionary with infinite distances
    g_score = {node: float('inf') for row in grid for node in row}  # Cost from start to each node
    g_score[start] = 0  # Cost from start to start is 0

    # Initialize f score dictionary with infinite distances
    f_score = {node: float('inf') for row in grid for node in row}  # Estimated total cost from start to end through each node
    f_score[start] = ((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)**0.5  # Heuristic for the start node
    
    open_list.append((f_score[start], start))  # Add the start node to the open list

    # Main loop continues until there is no node to evaluate
    while open_list:
        # Select the node in open_list with the lowest f score value
        current = min(open_list, key=lambda x: x[0])[1]
        open_list = [x for x in open_list if x[1] != current]  # Remove the current node from open list
        
        # Check if the current node is the end node
        if current == end:
            path = []  # Store the path from start to end
            while current in came_from:
                path.append(current)
                current = came_from[current]  # Traverse back from end to start
            path.append(start)  # Add the start node to the path
            path.reverse()  # Reverse the path to get it in correct order

            # Display debug messages
            display_message("Path points successfully created")
            display_message("Start location is " + str(start))

            return path  # Return the path
        
        closed_list.add(current)  # Mark the current node as evaluated

        # Check nodes in four directions(up, down, left, right)
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # Ensure neighbor is within grid bounds and is traversable (grid value of 1)
            if (0 <= neighbor[0] < COL) and (0 <= neighbor[1] < ROW) and grid[neighbor[0]][neighbor[1]] == 1:
                if neighbor in closed_list:  # Skip if neighbor is already evaluated
                    continue
                
                tentative_g_score = g_score[current] + 1  # Tentative g score
                
                # Discover a new node or find a better path to an already discovered node
                if neighbor not in [x[1] for x in open_list]:
                    came_from[neighbor] = current  # Update director
                    g_score[neighbor] = tentative_g_score  # Update g score
                    f_score[neighbor] = g_score[neighbor] + ((neighbor[0] - end[0]) ** 2 + (neighbor[1] - end[1]) ** 2)**0.5  # Update f score
                    open_list.append((f_score[neighbor], neighbor))  # Add neighbor to open list
                elif tentative_g_score < g_score[neighbor]:  # Check if this path to neighbor is better than previously found
                    came_from[neighbor] = current  # Update director
                    g_score[neighbor] = tentative_g_score  # Update g score
                    f_score[neighbor] = g_score[neighbor] + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])  # Update f score

                    # Update the neighbor node in the open list with the new f score
                    open_list = [(f, pos) for f, pos in open_list if pos != neighbor]
                    open_list.append((f_score[neighbor], neighbor))
    
    # If the loop finishes without returning a path, no path was found
    display_message("No path found")
    display_message("Start location is " + str(start))
    return []  # Return an empty path if no path is found


#end of file