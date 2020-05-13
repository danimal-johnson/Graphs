"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        traverse_queue = Queue()
        current_vertex = starting_vertex
        visited_nodes = []

        while current_vertex != None:
            for v in self.vertices[current_vertex]:
                if v not in visited_nodes:
                    traverse_queue.enqueue(v)
            visited_nodes.append(current_vertex)
            current_vertex = traverse_queue.dequeue()

        print(visited_nodes)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        traverse_stack = Stack()
        current_vertex = starting_vertex
        visited_nodes = []

        while current_vertex != None:
            if current_vertex not in visited_nodes:
                visited_nodes.append(current_vertex)
                for v in self.vertices[current_vertex]:
                    if v not in visited_nodes:
                        traverse_stack.push(v)
            current_vertex = traverse_stack.pop()

        print(visited_nodes)

    def dft_recursive(self, starting_vertex, visited=None, order=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        if order == None:
            order = []

        visited.add(starting_vertex)
        order.append(starting_vertex)

        print("Node ", starting_vertex)
        for child in self.vertices[starting_vertex]:
            if child not in visited:
                self.dft_recursive(child, visited, order)

        return order

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
        # Dequeue the first PATH
        # Grab the last vertex from the PATH
        # If that vertex has not been visited...
        # CHECK IF IT'S THE TARGET
        # IF SO, RETURN PATH
        # Mark it as visited...
        # Then add A PATH TO its neighbors to the back of the queue
        # _COPY_ THE PATH
        # APPEND THE NEIGHOR TO THE BACK

        search_queue = Queue()
        search_queue.enqueue([starting_vertex])
        visited_nodes = set()

        path = search_queue.dequeue()
        while path != None:
            current_vertex = path[-1]
            if current_vertex not in visited_nodes:
                if current_vertex == destination_vertex:
                    return path
                visited_nodes.add(current_vertex)
                for neighbor in self.vertices[current_vertex]:
                    new_path = list(path)  # COPY of path
                    new_path.append(neighbor)
                    search_queue.enqueue(new_path)
            path = search_queue.dequeue()

        return None  # No path found

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # FIXME: this is BFS (also, probably BS)
        # Create an empty stack and push A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the stack is not empty...
        # Pop the first PATH
        # Grab the last vertex from the PATH
        # If that vertex has not been visited...
        # CHECK IF IT'S THE TARGET
        # IF SO, RETURN PATH
        # Mark it as visited...
        # Then add A PATH TO its neighbors to the back of the queue
        # _COPY_ THE PATH
        # APPEND THE NEIGHOR TO THE BACK

        search_queue = Queue()
        search_queue.enqueue([starting_vertex])
        visited_nodes = set()

        path = search_queue.dequeue()
        while path != None:
            current_vertex = path[-1]
            if current_vertex not in visited_nodes:
                if current_vertex == destination_vertex:
                    return path
                visited_nodes.add(current_vertex)
                for neighbor in self.vertices[current_vertex]:
                    new_path = list(path)  # COPY of path
                    new_path.append(neighbor)
                    search_queue.enqueue(new_path)
            path = search_queue.dequeue()

        return None  # No path found

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        if path == None:
            path = []

        visited.add(starting_vertex)
        # path.append(starting_vertex)
        path = path + [starting_vertex]  # Make a COPY

        # Base case
        if starting_vertex == destination_vertex:
            return path

        # Go through each child node
        for child in self.vertices[starting_vertex]:
            # Drill down immediately (this is a depth-first search)
            if child not in visited:
                # Be careful not to pass by reference!
                new_path = self.dfs_recursive(
                    child, destination_vertex, visited, path)
                # If we're returning a path, it contains a valid route
                if new_path:
                    return new_path

        return None  # Not found


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
    print("Vertices:", graph.vertices)

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
    print("BFT(1):")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT(1):")
    graph.dft(1)

    print("DFT_Recursive(1):")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS(1,6):")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS(1,6):")
    # print(graph.dfs(1, 6))

    print("DFS Recursive(1,6):")
    print(graph.dfs_recursive(1, 6))
