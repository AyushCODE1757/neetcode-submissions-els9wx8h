class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = max(nums)
        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            temp = curMax * n
            curMax = max(temp, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
        return res
        