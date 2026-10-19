class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        k = 0
        for k, a in enumerate(nums):
            if k > 0 and a == nums[k - 1]:
                continue
            i = k + 1
            j = n - 1
            while i < j:
                threeSum = a + nums[i] + nums[j]
                if threeSum == 0:
                    res.append([a, nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                
                if threeSum < 0:
                    i += 1
                elif threeSum > 0:
                    j -= 1
        return res
