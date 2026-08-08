class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxHeap = [[-f, c] for c, f in freq.items()]
        heapq.heapify(maxHeap)
        res = ""
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            f, c = heapq.heappop(maxHeap)
            f += 1
            res += c
            if prev:
                heapq.heappush(maxHeap, prev)
                prev= None
            if f != 0:
                prev = [f, c]
        return res


            

        
        