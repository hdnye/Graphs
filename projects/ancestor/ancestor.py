
def earliest_ancestor(ancestors, starting_node):
    # Turn ancestors into adjacency list
    adjacency_list = {}

    for ancestor_pair in ancestors:
        # add both vertices to AL:
        if ancestor_pair[0] not in adjacency_list:
            adjacency_list[ancestor_pair[0]] = set()
        if ancestor_pair[1] not in adjacency_list:
            adjacency_list[ancestor_pair[1]] = set()
        # add the edge btn the vertices
        adjacency_list[ancestor_pair[1]].add(ancestor_pair[0])
    print(adjacency_list)

    # create a queue
    queue = [ [starting_node] ]
    # create a visted set of vertices
    visited = set()
    # keep track of the lengths of the paths to find the longest
    max_path_length = 1
    # keep track of cur earliest ancestor
    cur_earliest_ancestor = -1

    while len(queue) > 0:
        cur_path = queue.pop(0)
        print(cur_path)
        cur_vert = cur_path[-1]
        print(f' now on: {cur_vert}')
        if cur_vert not in visited:
            visited.add(cur_vert)
            # update max_path and check for tied path #s
            if len(cur_path) > max_path_length or len(cur_path) >= max_path_length and cur_vert < cur_earliest_ancestor:
                max_path_length = len(cur_path)
                cur_earliest_ancestor = cur_vert
            # find neighbors
            for neighbors in adjacency_list[cur_vert]:
                new_path = list(cur_path)
                new_path.append(neighbors)
                queue.append(new_path)

    return cur_earliest_ancestor 


"""
- Build graph
- Traverse graph
- Can use BFS or DFS

"""
