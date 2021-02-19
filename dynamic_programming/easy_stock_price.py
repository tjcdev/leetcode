# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        profit = 0
        for i in range(0, len(prices)):
            if (buy_price > prices[i]):
                buy_price = prices[i]
            else:
                profit = max([profit, prices[i]-buy_price])
        
        return profit