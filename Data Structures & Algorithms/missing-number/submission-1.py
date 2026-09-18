class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        total = 0 
        for num in nums:
            count += 1
            total += num
        return (count * (count + 1) // 2) - total