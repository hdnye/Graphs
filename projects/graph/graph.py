"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque
# Build the graph
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # if there's not edges, the id will be an empty set
        self.vertices[vertex_id] = set()           
     
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check to make sure the edges are in the list
        if v1 in self.vertices and v2 in self.vertices:
            # need 2 vertices parameter
            self.vertices[v1].add(v2)
        else:
            print('Error, vertext not found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # will return the set value of the id key
        return self.vertices[vertex_id]

    # Traversing the graph   
    def bft(self, starting_vertex_id):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Need to track cur_node & next_node to add to Queue
        # create empty queue & add starting vertex, will keep track of all next_to_visit_vertices
        queue = []
        queue.append(starting_vertex_id)
        # Create an empty set to keep track of all visited vertices
        visited = set()

        # while the queue is not empty:
        while len(queue) > 0:
            # dequeue a vertex off the queue
            cur_vertex = queue.pop(0)
            
            # if vertex not in visited: 
            if cur_vertex not in visited:                 
                # print it
                print(cur_vertex)

                # add the vertex to our visited set
                visited.add(cur_vertex)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(cur_vertex):
                    queue.append(neighbor)           
                

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create empty stack 
        stack = []
        stack.append(starting_vertex)
        # Create an empty set to keep track of all visited vertices
        visited = set()
        # while the stack is not empty:
        while len(stack) > 0:
            # pop a vertex off the stack
            cur_vertex = stack.pop(0)

            # if vertex not in visited:
            if cur_vertex not in visited:
                # print it
                print(cur_vertex)

                # add the vertex to our visited set
                visited.add(cur_vertex)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(cur_vertex):
                    stack.append(neighbor)
        

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO
    
    # this alg does BFT until target found & rtns arr of the vertex ids that are part of the path
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue & add a PATH_TO starting vertex
        # i.e. add array[1] to the queue
        queue = deque()
        queue.append(starting_vertex)
        # create visited set
        visited = set()  # check if current vortex is the target vortex
        if starting_vertex is destination_vertex:
            # found vertex & path to it
            # return PATH
            return queue
        # while queue is not empty:
        while len(queue) > 0:
            # dequeue the current PATH from the queue
            path = queue.popleft()
            # to get cur_vert to analyze from the PATH
            # use the vertex at the end of the path arr
            destination_vertex = path[-1]
            # if vertex not visited:
            # add vertex to visited
            if path not in visited:
                print(path)
                visited.add(path)
            # for each neigh of cur_vert
            elif destination_vertex not in visited:
                for neighbor in self.get_neighbors(destination_vertex):
                    # add path to the neigh to the queue
                    # add neigh to new path
                    new_path = list(path)
                    # Copy the current path
                    new_path.append(neighbor)
                    # add the whole path to queue
                    queue.append(new_path)
                    # return path if neighbor == dest_vertex
                    if neighbor is destination_vertex:
                        return new_path                  
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
