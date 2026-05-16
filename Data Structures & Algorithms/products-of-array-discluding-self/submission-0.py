class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_to_return = []
        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            num_to_add = 1
            for num in nums_copy:
                num_to_add *= num
            list_to_return.append(num_to_add)
        return list_to_return