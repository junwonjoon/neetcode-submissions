class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        for num in nums:
            index = length - 1 - abs(num)
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
        return 0
            