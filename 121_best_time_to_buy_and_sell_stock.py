class Solution:
    def maxProfit(self, prices) -> int:
        l = 0
        max_profit = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                current_profit = prices[r] - prices[l]
                max_profit = max(current_profit, max_profit)
            r += 1

        return max_profit

                
        