class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return_lst = [[]]

        for n in nums:
            lst = []
            for elem in return_lst:
                for i in range(len(elem) + 1):
                    elem_copy = elem.copy()
                    elem_copy.insert(i, n)
                    lst.append(elem_copy)
            return_lst = lst

        return return_lst 

