class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = {i: [] for i in range(vertices)}  

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.V

        self.dfs_util(start_vertex, visited)


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 3)

    print("DFS starting from vertex 0:")
    g.dfs(0)
