class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range( 2 ** len(nums)):
            binary_rep = f"{i:0{len(nums)}b}"
            subset = []
            print(binary_rep)
            for j in range(len(binary_rep)):
                    if j < len(nums) and binary_rep[j] == "1":
                        subset.append(nums[j])
            subsets.append(subset)
        
        return subsets
            
        
