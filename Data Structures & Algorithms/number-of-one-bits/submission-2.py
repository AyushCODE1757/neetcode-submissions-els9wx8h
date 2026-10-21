class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1
            print(bin(n))
            n >>= 1
        return cnt
        