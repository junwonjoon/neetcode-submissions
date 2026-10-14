class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = -11
        global_min = 11
        local_max = nums[0]
        local_min = nums[0]
        for num in nums[1:]:
            curr = local_max
            local_max = max(curr * num, local_min * num, num)
            local_min = min(curr * num, local_min * num, num)
            global_max = max(global_max, local_max)
            global_min = min(local_min, global_min)
        return max(global_max,local_max)