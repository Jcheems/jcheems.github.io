# Astar Algorithm path planner
## Introduction
The algorithm is mainly implemented in pathplanner.py and called by gui.py. The programme uses four directions (up, down, left, right) for path calculation. Obstacles are indicated by black squares. When a path is found, a blue path is shown in the gui connecting a green start point to a red end point.
<div align="center">
    <img src="./assets/images/Astar.gif" width="300px" display="inline"> 
    <div>
        <p>Example</p>
    </div>
</div>

## No path found
When no path is found, no path is planned and an error message is displayed in the window.
<div align="center">
    <img src="./assets/images/nopath.png" width="300px" display="inline"> 
    <div>
        <p>No path found</p>
    </div>
</div>

## Code Explanation
This Python code defines a function 'do_a_star' which implements the A* search algorithm for pathfinding on a grid. The function takes a grid, start and end points, and a function for displaying messages. Here's a step-by-step breakdown of what this code does:

### Initialization:
Retrieve the dimensions of the grid (COL and ROW).
Initialize open_list to store nodes that need to be evaluated and closed_list to store nodes that have already been evaluated.
Define came_from dictionary to track the path taken to reach each node.
Set up g_score dictionary to store the cost from the start node to every other node, initializing all values to infinity, except the start node which is set to zero.
Establish f_score dictionary to store the estimated total cost from the start node to the end through each node, initializing all values to infinity. The heuristic used is the Euclidean distance between the current node and the end node.

```Python
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

###Processing Loop:
Continuously loop until there are no more nodes to evaluate in the open_list.
Select the node in open_list with the lowest f score, make it the current node, and remove it from open_list.
Check if the current node is the end node. If it is, backtrack using the came_from dictionary to construct the path from start to end, display messages, and return the path.
Add the current node to the closed_list as it has been evaluated.

```python
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
```
