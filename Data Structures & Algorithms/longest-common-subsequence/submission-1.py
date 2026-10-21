class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        if n > m:
            self.longestCommonSubsequence(text2, text1)
        lcs = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
        return lcs[-1][-1]