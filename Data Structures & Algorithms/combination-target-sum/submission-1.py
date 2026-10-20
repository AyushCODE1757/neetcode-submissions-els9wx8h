class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(i, total=0):
            if total == target:
                res.append(comb.copy())
                return
            elif i == len(nums) or total > target:
                return
            comb.append(nums[i])
            total += nums[i]
            dfs(i, total)
            comb.pop()
            total -= nums[i]
            dfs(i + 1, total)
        dfs(0)
        return res
            