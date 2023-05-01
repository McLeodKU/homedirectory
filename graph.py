"""
Name: Michael Oliver
Date Created: April 30th 2023
Purpose: Python code for assignment eight 
"""
class Euler:

    def find_path(self, u, graph, visited_edge, path=[]):
        path = path + [u]   # Add the current node to the path
        for v in graph[u]:  # Traverse all neighbors of the current node
            if visited_edge[u][v] == False:
                visited_edge[u][v], visited_edge[v][u] = True, True # If not, mark the edge as visited in both directions
                path = self.find_path(v, graph, visited_edge, path)    # Recursively traverse the unvisited neighbor
        return path # Return the path traversed so far

    def check_circuit_or_path(self, graph, max_node):
        odd_degree_nodes = 0    # Initialize variables to count odd degree nodes and their indices
        odd_node = -1
        for i in range(max_node): # Loop through all nodes in the graph
            if i not in graph.keys():   # Skip nodes that are not in the graph
                continue
            if len(graph[i]) % 2 == 1:  # Check if the node has odd degree
                odd_degree_nodes += 1
                odd_node = i    # If so, increment the odd degree node count and update the odd node index
        if odd_degree_nodes == 0:    # Determine the type of circuit/path based on the number of odd degree nodes found
            return 1, odd_node  # EULER circuit
        if odd_degree_nodes == 2:
            return 2, odd_node  # EULER PATH
        return 3, odd_node

    def check_euler(self, graph, max_node):
        visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]   # Initialize the boolean matrix to track visited edges
        check, odd_node = self.check_circuit_or_path(graph, max_node)       # Check if the graph is Eulerian and if so, what type of circuit/path it has
        if check == 3:   # If the graph is neither a circuit nor a path, print an error message and return
            print("graph is not Eulerian")
            print("no path")
            return
        start_node = 1  # Otherwise, determine the starting node for the DFS traversal
        if check == 2:
            start_node = odd_node
            print("graph has a Euler path")
        if check == 1:
            print("graph has a Euler cycle")
        path = self.find_path(start_node, graph, visited_edge)    # Traverse the graph using DFS from the starting node and store the path
        path = self.print_help(path)    # Convert node indices to letters for readability and return the new path
        output = ""
        for i in path:
            output += i + "-"
        output = output[:-1]
        print(output)       # Format and print the path as a string

    def print_help(self, path): # Map node indices to letters for readability
        letters = 'abcdefghijklmnopqrstuvwxyz'
        label_map = dict(zip(range(1, len(letters) + 1), letters))
        return [label_map[node] for node in path]       # Convert each node index in the path to its corresponding letter
    

class Hamilton:

    def has_hamiltonian_cycle_ore(self, graph):
        n = len(graph)
        for u in graph:
            for v in graph:
                if u != v and v not in graph[u]: # check if u and v are non-adjacent vertices
                    degree_sum = len(graph[u]) + len(graph[v]) # compute the sum of their degrees
                    if degree_sum < n: # check if the degree sum condition is violated
                        return False # the graph is not Hamiltonian by Ore's theorem
        return True # the graph is Hamiltonian by Ore's theorem

    def is_hamiltonian_ore(self, graph):
        if self.has_hamiltonian_cycle_ore(graph):
            print("The graph has a Hamiltonian cycle by Ore's theorem.")
        else:
            print("The graph does not have a Hamiltonian cycle by Ore's theorem.")

    def has_hamiltonian_cycle_dirac(self, graph):
        n = len(graph)
        for vertex in graph:
            degree = len(graph[vertex])
            if degree < n/2: # check if the degree condition is violated
                return False # the graph is not Hamiltonian by Dirac's theorem
        return True # the graph is Hamiltonian by Dirac's theorem

    def is_hamiltonian_dirac(self, graph):
        if self.has_hamiltonian_cycle_dirac(graph):
            print("The graph has a Hamiltonian cycle by Dirac's theorem.")
        else:
            print("The graph does not have a Hamiltonian cycle by Dirac's theorem.")