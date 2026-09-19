class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        rob1_p, rob1_c, rob2_c, rob2_p = 0, 0, 0, 0
        for n in nums[:-1]:
            temp = max(rob1_p + n, rob1_c)
            rob1_p = rob1_c 
            rob1_c = temp
        for n in nums[1:]:
            temp = max(rob2_p + n, rob2_c)
            rob2_p = rob2_c 
            rob2_c = temp
        return max(rob2_c, rob1_c)