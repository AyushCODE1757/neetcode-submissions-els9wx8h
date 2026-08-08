from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res |= n
        return res << len(nums) - 1

            

        