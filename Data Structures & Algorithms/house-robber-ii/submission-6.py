class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        def robHouses(nums):
            n = len(nums)
            skip = 0
            noSkip = nums[0]
            for i in range(1, n):
                skip, noSkip = max(noSkip, skip), skip + nums[i]
            return max(skip, noSkip)
        return max(robHouses(nums[:n - 1]), robHouses(nums[1: n]))


        