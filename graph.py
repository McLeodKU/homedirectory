from math import ceil
class Euler:

    def dfs(self, u, graph, visited_edge, path=[]):
        path = path + [u]
        for v in graph[u]:
            if visited_edge[u][v] == False:
                visited_edge[u][v], visited_edge[v][u] = True, True
                path = self.dfs(v, graph, visited_edge, path)
        return path

    def check_circuit_or_path(self, graph, max_node):
        odd_degree_nodes = 0
        odd_node = -1
        for i in range(max_node):
            if i not in graph.keys():
                continue
            if len(graph[i]) % 2 == 1:
                odd_degree_nodes += 1
                odd_node = i
        if odd_degree_nodes == 0:
            return 1, odd_node
        if odd_degree_nodes == 2:
            return 2, odd_node
        return 3, odd_node

    def check_euler(self, graph, max_node):
        visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
        check, odd_node = self.check_circuit_or_path(graph, max_node)
        if check == 3:
            print("graph is not Eulerian")
            print("no path")
            return
        start_node = 1
        if check == 2:
            start_node = odd_node
            print("graph has a Euler path")
        if check == 1:
            print("graph has a Euler cycle")
        path = self.dfs(start_node, graph, visited_edge)
        path = self.print_help(path)
        output = ""
        for i in path:
            output += i + "-"
        output = output[:-1]
        print(output)

    def print_help(self, path):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        label_map = dict(zip(range(1, len(letters) + 1), letters))
        return [label_map[node] for node in path]
    

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