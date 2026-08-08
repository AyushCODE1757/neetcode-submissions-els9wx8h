class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, sels):
            if i > n:
                if len(sels) == k:
                    res.append(sels)
                return
            dfs(i + 1, sels + [i])
            dfs(i + 1, sels)
        dfs(1, [])
        return res


        