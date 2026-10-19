class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = Counter(nums)
        nums = list(hashMap.keys())
        nums.sort(key=lambda x: hashMap[x], reverse=True)
        return nums[:k]