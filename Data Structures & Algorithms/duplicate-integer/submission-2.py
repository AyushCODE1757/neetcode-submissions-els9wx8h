class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(x > 1 for x in Counter(nums).values())