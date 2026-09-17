class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        used = set()
        first_t = True 
        while total not in used:
            if first_t:
                first_t = False
                total = n
            used.add(total)
            new_total = 0
            for num in [int(x) for x in str(total)]:
                new_total += num ** 2
            total = new_total
            print(total)
            if total == 1:
                return True
        return False