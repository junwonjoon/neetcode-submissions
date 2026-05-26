class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        i =0
        while i < len(prices):
            if i + 1 < len(prices) and prices[i+1] - prices[i] < 0 :
                i += 1
                continue
            for j in range(i,len(prices)):
                current_max = max(current_max, prices[j] - prices[i])
            i += 1
        return current_max