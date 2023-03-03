class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                if maxP < prices[r] - prices[l]:
                    maxP = prices[r] - prices[l]
                r += 1
        
        ### MY WAY BELOW ###
        # lowest = prices[0]
        # profit = 0
        # currentDiff = 0
        # for val in prices:
        #     if val < lowest:
        #         lowest = val
        #     else:
        #         currentDiff = val - lowest
        #         if currentDiff > profit:
        #             profit = currentDiff
        
        
        return maxP