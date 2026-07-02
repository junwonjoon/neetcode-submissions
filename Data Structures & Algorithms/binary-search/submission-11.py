from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        probable = bisect_left(nums, target)
        return probable if probable < len(nums) and nums[probable] == target else -1