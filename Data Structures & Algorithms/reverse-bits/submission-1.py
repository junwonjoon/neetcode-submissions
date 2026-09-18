class Solution:
    def reverseBits(self, n: int) -> int:
        compare = 1
        bin_str = ""
        while compare <= n:
            if n & compare:
                bin_str += "1"
            else:
                bin_str += "0"
            compare <<= 1
        while len(bin_str) < 32:
            bin_str += "0"
        total = 0 
        index = 1
        for binary in bin_str[::-1]:
            if binary == "1":
                total += index
            index <<= 1
        return total 