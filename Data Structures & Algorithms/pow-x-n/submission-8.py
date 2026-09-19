class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        answer = 1
        power = abs(n)

        while power:
            if power & 1:
                answer *= x
            x *= x
            power >>= 1

        return answer if n >= 0 else 1 / answer