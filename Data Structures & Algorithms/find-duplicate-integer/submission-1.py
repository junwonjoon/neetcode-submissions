class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #not a solution
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] >= 2:
                return num
            