class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        skip = 0
        noSkip = nums[0]
        for i in range(1, n):
            skip, noSkip = max(noSkip, skip), skip + nums[i]
            
        return max(skip, noSkip)