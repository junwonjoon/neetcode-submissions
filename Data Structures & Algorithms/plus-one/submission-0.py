class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        alpha_digits = ""
        for num in digits:
            alpha_digits += f"{num}"
        digits_plus_one = int(alpha_digits) + 1
        alpha_digits = str(digits_plus_one)
        return [int(x) for x in alpha_digits]