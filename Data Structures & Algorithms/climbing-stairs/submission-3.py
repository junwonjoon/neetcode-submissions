class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 0
        prev2 = 1
        curr = 0
        for _ in range(0, n):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return curr

        