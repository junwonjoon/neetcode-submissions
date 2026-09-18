class Solution:
    def rob(self, nums: List[int]) -> int:
        initial = 0
        local_max = 0
        for curr in nums:
            temp = max(local_max, initial + curr)
            initial = local_max 
            local_max = temp
        return local_max