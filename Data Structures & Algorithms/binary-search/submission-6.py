class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = len(nums) // 2
        index_keeper = 0
        while True:
            if nums[i] == target:
                return i + index_keeper
            elif len(nums) == 1:
                if nums[0] == target:
                    return 0
                else: 
                    return -1
            elif nums[i] > target:
                nums = nums[:i]
                index_keeper = 0
            elif nums[i] < target:
                nums = nums[i:]
                index_keeper += i
            i = len(nums) // 2