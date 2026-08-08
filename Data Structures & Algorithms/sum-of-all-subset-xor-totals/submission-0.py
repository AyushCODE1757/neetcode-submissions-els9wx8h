from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(cands, i):
            nonlocal res
            if i == len(nums):
                res += reduce(lambda x, y: x ^ y, cands, cands[0])
                return
            backtrack(cands + [nums[i]], i + 1)
            backtrack(cands, i + 1)
        backtrack([0], 0)
        return res

            

        