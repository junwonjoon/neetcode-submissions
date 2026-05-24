class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r_i = 1
        i = 0
        lst = []
        while True:
            if numbers[i] + numbers[-r_i] == target:
                return [i + 1, numbers.index(numbers[-r_i])+ 1]
            elif numbers[i] + numbers[-r_i] < target:
                i += 1
            elif numbers[i] + numbers[-r_i] > target:
                r_i += 1
                if numbers[i] > numbers[-r_i]:
                    r_i = 1
                    i += 1
        return []

