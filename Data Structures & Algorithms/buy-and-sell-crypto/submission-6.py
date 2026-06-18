class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Initizalize two pointers at i = 0, 1
        # Set max profit var = 0
        # 2. While right < len(prices)
        # 3. If the right pointer price is greater than the left pointer price,
        # calculate the current profit
            # If it is, then take the greater of the max and current profit
            # and update the max profit variable
        # If not, then we set the left pointer to the right pointer
        # increment the right pointer
        # Return max profit

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            
            right += 1
        
        return max_profit