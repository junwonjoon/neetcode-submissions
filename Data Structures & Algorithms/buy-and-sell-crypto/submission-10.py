class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        current_max = 0
        lp, rp = 0,1
        while rp < len(prices):
            if  prices[lp] < prices[rp]:
                current_max = max(current_max, prices[rp] - prices[lp])
            else:
               lp = rp
            rp += 1
        return current_max