from bisect import bisect_left
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        lst_to_return = []
        nums.sort()
        checked = set()
        i = 0
        max_len = len(nums) - 1
        while i < max_len:
            if nums[i] > 0:
                break
            if nums[i] in checked:
                i = bisect_left(nums, nums[i]+1)
                if i > max_len:
                    break
            checked.add(nums[i])
            target = -nums[i]
            checked_twoSum = set()
            l = i + 1
            r = max_len
            while l < max_len + 1 and l < r:
                if nums[l] > target:
                    break
                if nums[l] in checked_twoSum:
                    l = bisect_left(nums, nums[l] + 1)
                    if l > max_len:
                        break
                if nums[l] + nums[r] == target:
                    checked_twoSum.add(nums[l])
                    lst_to_return.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
        return lst_to_return    

