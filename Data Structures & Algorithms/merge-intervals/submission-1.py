class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for l, r in intervals:
            if merged and not(merged[-1][0] > r or merged[-1][1] < l):
                l1, r1 = merged.pop()
                merged.append([min(l1, l), max(r1, r)])
            else:
                merged.append([l, r])
        return merged