class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        visited = set([(0, 0)])
        pacific = set()
        atlantic = set()
        q = deque()
        for i in range(m):
            q.append((0, i))
            visited.add((0, i))
        for j in range(n):
            q.append((j, 0))
            visited.add((j, 0))
        for i in range(n):
            pacific.add((i, 0))
        for j in range(m):
            pacific.add((0, j))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < n and 
                    0 <= nc < m and 
                    (nr, nc) not in visited and 
                    heights[nr][nc] >= heights[r][c]):
                    pacific.add((nr, nc))
                    visited.add((nr, nc))
                    q.append((nr, nc))
        visited = {(n - 1, m - 1)}
        q = deque()
        for i in range(n):
            atlantic.add((i, m - 1))
            visited.add((i, m - 1))
            q.append((i, m - 1))
        for j in range(m):
            atlantic.add((n - 1, j))
            visited.add((n - 1, j))
            q.append((n - 1, j))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < n and 
                    0 <= nc < m and 
                    (nr, nc) not in visited and 
                    heights[nr][nc] >= heights[r][c]):
                    atlantic.add((nr, nc))
                    visited.add((nr, nc))
                    q.append((nr, nc))
        cells = set.intersection(pacific, atlantic)
        return [[r, c] for r, c in cells]

        





        