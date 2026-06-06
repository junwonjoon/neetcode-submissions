class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        elif len(s2) == len(s1):
            test_lst = sorted(list(s2))
            s1_lst = sorted(list(s1))
            for i in range(len(test_lst)):
                if test_lst[i] == s1_lst[i]:
                    continue
                else:
                    break
            else:
                return True
            return False
        else:
            l = 0 
            r = len(s1)
            while r <= len(s2):
                if s2[l] not in s1:
                    l += 1 
                    r += 1
                test_lst = sorted(list(s2[l:r]))
                s1_lst = sorted(list(s1))
                for i in range(len(test_lst)):
                    if test_lst[i] == s1_lst[i]:
                        continue
                    else:
                        break
                else:
                    return True
                l += 1
                r += 1
            return False
                    

