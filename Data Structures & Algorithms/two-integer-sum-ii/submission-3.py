class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r_i = 1
        i = 0
        lst = []
        while i < len(numbers):
            s_num, b_num = numbers[i], numbers[-r_i]
            if s_num + b_num == target:
                return [i + 1, len(numbers) - r_i + 1]
            elif s_num + b_num < target:
                i += 1
            elif s_num + b_num > target:
                r_i += 1
                if s_num > b_num:
                    r_i = 1
                    i += 1
        return []

