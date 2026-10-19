class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        n = len(s)
        maxFreq = 0
        counts = {}
        for r in range(n):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            while r - l + 1 - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            maxFreq = max(maxFreq, r - l + 1)
        return maxFreq
                        