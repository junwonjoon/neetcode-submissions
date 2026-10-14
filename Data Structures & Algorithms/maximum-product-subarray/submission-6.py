class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        global_max = local_max = local_min = nums[0]
        for num in nums[1:]:
            curr = local_max * num
            local_max = max(curr, local_min * num, num)
            local_min = min(curr, local_min * num, num)
            global_max = max(global_max, local_max)
        return global_max