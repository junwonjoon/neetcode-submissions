from bisect import bisect_left
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final_lst = []
        queue = [[num] for num in nums]
        duplicate = set()
        checked = set()
        nums.sort()
        if target < nums[0]:
            return []
        while queue:
            lst = queue.pop()
            temp = lst.copy()
            sum_lst = sum(lst)
            if sum_lst == target:
                tuple_lst = tuple(lst)
                if tuple_lst not in duplicate:
                    final_lst.append(lst)
                    duplicate.add(tuple_lst)  
            if tuple(lst) in checked:
                continue  
            checked.add(tuple(lst)) 
            for num in nums:
                if num + sum_lst > target:
                    break
                lst_ = temp.copy()
                index = bisect_left(lst_, num)
                lst_.insert(index, num)
                queue.append(lst_)
        return final_lst
            

