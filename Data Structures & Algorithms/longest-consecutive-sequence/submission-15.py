class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(list(set(nums))) == 1:
            return 1
        num_to_check = set()
        for number in nums:
            num_to_check.add(number + 1)
            num_to_check.add(number - 1)
        counter = 0
        lst = []
        for number in nums:
            if number in num_to_check:
                lst.append(number)
        if not lst:
            return 1
        max_sequence = 1
        new_sequence = 1
        lst = list(set(lst))
        lst.sort()
        prev = lst[0]
        print(lst)
        for i in range(1, len(lst)):
            print(prev + 1, lst[i])
            if prev + 1 == lst[i]:
                new_sequence += 1
            else:
                new_sequence = 1
            max_sequence = max(max_sequence, new_sequence)
            prev = lst[i]
        return max_sequence