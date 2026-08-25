class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        total_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                total_profit += prices[right] - prices[left]
            
            left = right
            right += 1
        
        return total_profit