class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        total = sum(nums)
        return (count * (count + 1) // 2) - total