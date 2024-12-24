class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class KruskalAlgorithm:
    @staticmethod
    def kruskal(vertices, edges):
        edges.sort()  # Sort edges by weight
        ds = DisjointSet(vertices)
        mst = []
        total_weight = 0

        for edge in edges:
            # Check if the edge forms a cycle
            if ds.find(edge.source) != ds.find(edge.destination):
                mst.append(edge)
                total_weight += edge.weight
                ds.union(edge.source, edge.destination)

            # Stop if MST contains V-1 edges
            if len(mst) == vertices - 1:
                break

        return mst, total_weight


# Example Usage
vertices = 5
edges = [
    Edge(0, 1, 7),
    Edge(0, 3, 8),
    Edge(1, 2, 5),
    Edge(1, 3, 9),
    Edge(1, 4, 7),
    Edge(2, 4, 8),
    Edge(3, 4, 5),
]

mst, total_weight = KruskalAlgorithm.kruskal(vertices, edges)

print("Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(f"({edge.source}, {edge.destination}) - Weight: {edge.weight}")

print(f"Total Weight of the MST: {total_weight}")
