class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        used = set()
        total = 0 
        for num in [int(x) for x in str(n)]:
            total += num ** 2
        if total == 1:
            return True
        while total not in used:
            used.add(total)
            new_total = 0
            for num in [int(x) for x in str(total)]:
                new_total += num ** 2
            total = new_total
            print(total)
            if total == 1:
                return True
        return False