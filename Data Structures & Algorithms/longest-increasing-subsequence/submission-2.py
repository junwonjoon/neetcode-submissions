from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length_i = [0] * len(nums)
        for i in range(len(length_i)):
            max_lis_so_far = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_lis_so_far = max(max_lis_so_far, length_i[j])
            length_i[i] = max(1, 1 + max_lis_so_far)
        return max(length_i)
