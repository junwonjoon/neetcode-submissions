class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = local_max = local_min = nums[0]
        for num in nums[1:]:
            curr = local_max * num
            local_max = max(curr, local_min * num, num)
            local_min = min(curr, local_min * num, num)
            global_max = max(global_max, local_max)
        return max(global_max,local_max)