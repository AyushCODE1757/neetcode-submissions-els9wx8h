class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myNums = set(nums)
        maxStreak = 0
        for n in myNums:
            m = n - 1
            streak = 0
            if n - 1 not in myNums:
                streak += 1
                j = n + 1
                while j in myNums:
                    j += 1
                    streak += 1
            maxStreak = max(streak, maxStreak)
        return maxStreak