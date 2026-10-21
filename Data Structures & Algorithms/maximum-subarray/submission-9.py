class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curSum = 0
        maxSum = nums[0]
        for r in range(n):
            if curSum < 0:
                curSum  = 0
            curSum += nums[r]
            maxSum = max(curSum, maxSum)
        return maxSum

        