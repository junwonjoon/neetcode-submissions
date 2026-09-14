class Solution:
    def countBits(self, n: int) -> List[int]:
        return_lst = []
        for i in range(n + 1 ):
            return_lst.append(f"{i:b}".count("1"))
        return return_lst