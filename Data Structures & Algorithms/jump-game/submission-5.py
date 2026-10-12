class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False] * len(nums)
        can_reach[0] = True
        for i in range(len(nums)):
            jump = nums[i] + i if can_reach[i] else 0
            if jump >= len(nums):
                return True
            for j in range(i,jump + 1):
                can_reach[j] = True
        return can_reach[-1]