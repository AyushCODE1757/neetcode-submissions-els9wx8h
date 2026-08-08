class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        t = sum(nums)
        if t % k != 0:
            return False
        t =  t // k
        sets = [0] * k
        nums.sort(reverse = True)
        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(k):
                if sets[j] + nums[i] <= t:
                    sets[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    sets[j] -= nums[i]
                if sets[j] == 0:
                    break
            return False
        return backtrack(0)
                

        