class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False] * len(nums)
        can_reach[0] = True
        length = len(nums)
        for i in range(length):
            jump = nums[i] + i if can_reach[i] else 0
            for j in range(i,jump + 1):
                if j >= length:
                    return True
                can_reach[j] = True
        return can_reach[-1]