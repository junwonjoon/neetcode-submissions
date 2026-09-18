class Solution:
    def hammingWeight(self, n: int) -> int:
        compare = 1
        count = 0
        while compare <= n:
            count += 1 if compare & n else 0
            compare <<= 1
        return count