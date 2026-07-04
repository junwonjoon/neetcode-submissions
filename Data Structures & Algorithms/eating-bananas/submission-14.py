from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate_ub = 0 
        sum_piles = 0
        for pile in piles:
            sum_piles += pile
            rate_ub = max(rate_ub, pile)
        rate_lb = ceil(sum_piles/h)
        rate = rate_lb
        if verify(piles, rate, h):
            return rate
        else:
            while rate_lb < rate_ub:
                rate = (rate_lb + rate_ub) // 2 
                if verify(piles, rate, h):
                    rate_ub = rate
                else:
                    rate_lb = rate + 1
            return rate_lb         

def verify(piles, cand, h):
    hours = 0
    for elem in piles:
        hours += ceil(elem/cand)
        if hours > h:
            return False
    else:
        return True