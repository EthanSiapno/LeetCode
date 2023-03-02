class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        currentDiff = 0
        for val in prices:
            if val < lowest:
                lowest = val
            else:
                currentDiff = val - lowest
                if currentDiff > profit:
                    profit = currentDiff
        
        
        return profit