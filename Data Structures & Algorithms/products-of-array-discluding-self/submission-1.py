class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, post = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(n - 1, -1, -1):
            post[i] = post[i + 1] * nums[i]
        return [pref[i] * post[i + 1] for i in range(n)]
        
