class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            cnt = 0
            while n:
                cnt += n & 1
                print(bin(n))
                n >>= 1
            return cnt
        return [hammingWeight(i) for i in range(n + 1)]
