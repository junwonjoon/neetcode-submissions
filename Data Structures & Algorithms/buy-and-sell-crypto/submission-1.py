class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                current_max = max(current_max, prices[j] - prices[i])
        return current_max