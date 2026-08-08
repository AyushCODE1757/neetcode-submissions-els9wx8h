class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        bus = []
        curPass = 0

        for numPass, start, end in trips:
            while bus and bus[0][0] <= start:
                curPass -= heapq.heappop(bus)[1]
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(bus, [end, numPass])
        return True       