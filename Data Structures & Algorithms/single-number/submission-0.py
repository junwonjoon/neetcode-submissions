class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_ = set()
        set_2 = set()
        for num in nums:
            if num in set_:
                set_2.add(num)
            set_.add(num)
        return (set_ - set_2).pop()
