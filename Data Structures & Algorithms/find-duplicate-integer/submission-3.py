class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        digits = 2
        magic = 0
        for num in nums:
            bit_num = 1 << num
            if bit_num ^ magic < magic:
                return num
            magic += bit_num
        return 0
        
            