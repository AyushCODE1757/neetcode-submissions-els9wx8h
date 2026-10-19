class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        n = len(prices)
        currMax = 0
        while r < n:
            if prices[r] < prices[l]:
                l = r 
            else:
                profit = prices[r] - prices[l]
                currMax = max(profit, currMax)
            r += 1
        return currMax
            
            

        