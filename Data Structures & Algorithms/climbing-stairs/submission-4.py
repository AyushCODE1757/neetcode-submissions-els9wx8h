class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 1
        for i in range(n - 2, -1, -1):
            a, b = a + b, a
        return a