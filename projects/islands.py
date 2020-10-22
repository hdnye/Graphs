'''
Connected Components: lists in graphs not connected to other lists directly

Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4

    - Count the # of connected components & keep track of visited
    - turn into a graph
    - what would a vertex be?
        - let 1's be vertices
    - what are the edges? 
        - 2 vertices are connected if they are NSEW from each other
'''

def get_neigboring_vertices(row, col, islands):
    neighbors = [] # return tuples of coordinates
    # check North
    if row > 0 and islands[row -1][col] == 1:
        neighbors.append( ( row-1, col) )
    # check South
    if row < len(islands) - 1 and islands[row + 1][col] == 1:
        neighbors.append( ( row + 1, col) )
    # check West
    if col > 0 and islands[row][col - 1] == 1:
        neighbors.append( (row, col -1) )
    # check East
    if col < len(islands[0]) - 1 and islands[row][col + 1] == 1:
        neighbors.append((row, col + 1))
    return neighbors

def dft(row, col, islands, visited):
    # share visited set from parent f()
    stack = [ ( row, col ) ]

    while len(stack) > 0:
        cur_vert = stack.pop()
        cur_row = cur_vert[0]
        cur_col = cur_vert[1]

        if not visited[cur_row][cur_col]:
            visited[cur_row][cur_col] = True
            # get neighbors
            for neighbors in get_neigboring_vertices(cur_row, cur_col, islands):
                stack.append(neighbors)        


def island_counter(islands):
    # Create DS to keep track of seen 
    visited = []
    for i in range(len(islands)):
        # creates array of all false counters
        visited.append([False] * len(islands[0]))

    # keep count of islands seen
    island_count = 0
    # 2 for loops for columns & rows
    for row in range(len(islands[0])):
        for col in range(len(islands[0])):
            if not visited[row][col]:
                # if we reach a 1
                cur_value = islands[row][col]  
                if cur_value == 1:
                    # traverse the island's array using either BFT/DFT
                    dft(row, col, islands, visited)
                    island_count += 1
                else: 
                    visited[row][col] = True

    return island_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))