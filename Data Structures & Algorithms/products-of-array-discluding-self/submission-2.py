class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        index = -1
        product_without_zero = 1
        for number in nums:
            index += 1
            product *= number
            if number == 0:
                zero_count += 1
            else:
                product_without_zero *= number
            if zero_count > 1:
                break

        if zero_count > 1:
            return [0 for _ in range(len(nums))]
        elif zero_count == 1:
            return [0 if number != 0 else product_without_zero for number in nums]
        else:
            return [product//number for number in nums]

            