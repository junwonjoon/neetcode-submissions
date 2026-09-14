class Solution:
    def countBits(self, n: int) -> List[int]:
        return_lst = []
        for i in range(n + 1):
            num = 0
            for j in f"{i:b}":
                if j == "1":
                    num += 1
            return_lst.append(num)
        return return_lst