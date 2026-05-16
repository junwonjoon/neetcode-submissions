class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = len(nums)
        for i in range(index):
            for j in range(index -1 ,-1,-1):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i,j]