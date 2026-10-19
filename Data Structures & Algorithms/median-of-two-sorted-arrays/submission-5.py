class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, n1
        INF = float('inf')
        while low <= high:
            i = low + (high - low) // 2
            j = ((n1 + n2 + 1) // 2) - i
            lA = -INF if i == 0 else nums1[i - 1]
            lB = -INF if j == 0 else nums2[j - 1]
            rA = INF if i == n1 else nums1[i]
            rB = INF if j == n2 else nums2[j]
            if lB > rA:
                low = i + 1
            elif lA > rB:
                high = i - 1
            else:
                if ((n1 + n2) % 2) == 0:
                    return (max(lA, lB) + min(rA, rB)) / 2.0
                else:
                    return max(lA, lB)
            

        


        