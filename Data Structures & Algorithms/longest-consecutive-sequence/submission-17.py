class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new_nums = list(set(nums))
        if len(new_nums) <= 1:
            return 1
        new_nums.sort()
        prev = new_nums[0]
        new_sequence = 1
        max_sequence = 1
        for i in range(1,len(new_nums)):
            if prev + 1 == new_nums[i]:
                new_sequence += 1
            else:
                new_sequence = 1
            max_sequence = max(max_sequence, new_sequence)
            prev = new_nums[i]
        return max_sequence