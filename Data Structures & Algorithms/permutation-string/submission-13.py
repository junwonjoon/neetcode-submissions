class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l = 0 
        r = len(s1)
        s1 = sorted(s1)
        while r <= len(s2):
            test = sorted(s2[l:r])
            if s1 == test:
                return True
            l += 1
            r += 1
        return False
                

