class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = -11
        prev_min = 11
        curr_max = nums[0]
        curr_min = nums[0]
        for num in nums[1:]:
            curr = curr_max
            curr_max = max(curr * num, curr_min * num, num)
            curr_min = min(curr * num, curr_min * num, num)
            prev_max = max(prev_max, curr_max)
            prev_min = min(curr_min, prev_min)
            # print(curr_max, curr_min, prev_max, prev_min)
        return max(prev_max,curr_max)