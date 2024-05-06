# Astar Algorithm path planner
## Introduction
The algorithm is mainly implemented in pathplanner.py and called by gui.py. The programme uses four directions (up, down, left, right) for path calculation.
<div align="center">
    <img src="./assets/images/Astar.gif" width="300px" display="inline"> 
    <div>
        <p>Example</p>
    </div>
</div>

## Code ExplanationThis
Python code defines a function 'do_a_star' which implements the A* search algorithm for pathfinding on a grid. The function takes a grid, start and end points, and a function for displaying messages. Here's a step-by-step breakdown of what this code does:

### Initialization:
Retrieve the dimensions of the grid (COL and ROW).
Initialize open_list to store nodes that need to be evaluated and closed_list to store nodes that have already been evaluated.
Define came_from dictionary to track the path taken to reach each node.
Set up g_score dictionary to store the cost from the start node to every other node, initializing all values to infinity, except the start node which is set to zero.
Establish f_score dictionary to store the estimated total cost from the start node to the end through each node, initializing all values to infinity. The heuristic used is the Euclidean distance between the current node and the end node.
    ```python
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
    ```
