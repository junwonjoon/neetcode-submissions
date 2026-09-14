class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(1 << len(nums)):
            subsets.append([nums[j] for j in range(len(nums)) if i & (1 << j)])
        return subsets
            
        
