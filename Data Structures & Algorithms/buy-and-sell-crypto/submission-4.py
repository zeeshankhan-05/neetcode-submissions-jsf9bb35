class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Iterate through the prices
        # For each price, check if the next price is greater than the current price
            # If not, move to the next price (increment)
            # If it is, compare the current profit against the max profit found
        # Continue until the prices array is finished iterating
        # Return the max profit

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right
            
            right += 1

        return max_profit