class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        cnt = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(n):
            for c in range(m):
                if (r, c) not in visited and grid[r][c] == '1':
                    cnt += 1
                    q = deque([(r, c)])
                    visited.add((r, c))
                    while q:
                        r, c = q.popleft()
                        for dr, dc in dirs:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] == '1':
                                q.append((nr, nc))
                                visited.add((nr, nc))
        return cnt 
                                

        
        