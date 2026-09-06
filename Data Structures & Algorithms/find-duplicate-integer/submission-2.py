class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #not an optimal solution
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] >= 2:
                return num
            