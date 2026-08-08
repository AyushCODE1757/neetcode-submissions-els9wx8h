class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for f, ch in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if f:
                heapq.heappush(heap, (f, ch))
        res = ""
        while heap:
            f, ch = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not heap:
                    break
                f2, c2 = heapq.heappop(heap)
                f2 += 1
                res += c2
                if f2:
                    heapq.heappush(heap, (f2, c2))
                heapq.heappush(heap, (f, ch))
            else:
                res += ch
                f += 1
                if f:
                    heapq.heappush(heap, (f, ch))
        return res


        