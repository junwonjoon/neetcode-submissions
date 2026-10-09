class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans_s = set()
        for i in range(2 ** len(nums)):
            binary = f"{i:0{len(nums)}b}"
            temp_set = []
            print(binary)
            for j in range(len(binary)):
                if binary[j] == "1":
                    temp_set.append(nums[j])
            temp_s = sorted(temp_set)
            if tuple(temp_s) not in ans_s:
                ans_s.add(tuple(temp_s))
        return [list(x) for x in ans_s]
