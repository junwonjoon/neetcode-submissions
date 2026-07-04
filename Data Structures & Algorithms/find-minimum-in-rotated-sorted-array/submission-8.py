class Solution:
    def findMin(self, nums: List[int]) -> int:
            l, r = 0, len(nums) - 1
            m = 0
            while l < r:
                m = (l + r) // 2
                if nums[l] < nums[r]:
                    return nums[l]
                elif r - l == 1 and nums[l] > nums[r]:
                    return nums[r]
                elif nums[m] > nums[l]:
                    l = m + 1
                else:
                    r = m
            return nums[l]