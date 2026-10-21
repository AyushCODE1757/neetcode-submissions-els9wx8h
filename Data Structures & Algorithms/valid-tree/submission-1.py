class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            if not adjList[node]:
                return True
            for v in adjList[node]:
                if v != parent and not dfs(v, node):
                    return False
            return True
        return dfs(0, 0) and len(visited) == n
        
