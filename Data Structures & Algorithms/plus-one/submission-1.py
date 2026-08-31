class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_digits = 0
        digit = 1
        
        for i in range(1, len(digits)+1):
            num_digits += digits[-i] * digit
            digit *= 10
        num_digits += 1
        return [int(x) for x in str(num_digits)]