class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_digits = 0
        digit = 1
        digit_increment = False
        digits[-1] = digits[-1] + 1
        len_digits = len(digits)
        for i in range(1, len_digits +1):
            print(digits[-i])
            if digits[-i] >= 10: 
                digits[-i] %= 10
                if -i-1 >= -len_digits:
                    digits[-i-1] += 1
                else:
                    digits.insert(0,1)
        return digits