class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
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
            else:
                break
        return digits