class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        x, y = self.find(u), self.find(v)
        if x == y:
            return False
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        visited = set()
        for i in range(n):
            visited.add(dsu.find(i))
        return len(visited)

        