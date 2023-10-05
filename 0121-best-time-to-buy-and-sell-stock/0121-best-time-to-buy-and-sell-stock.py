class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        currentProfit = 0
        currentLow = prices[0]
        
        for price in prices:
            if price < currentLow:
                currentLow = price
            
            currentProfit = price - currentLow
            if currentProfit > maxP:
                maxP = currentProfit
        
        return maxP