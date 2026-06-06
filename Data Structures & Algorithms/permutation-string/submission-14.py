class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l = 0 
        r = len(s1)
        s1_dict = {}
        for letter in s1:
            s1_dict[letter] = 1 + s1_dict.get(letter, 0)
        while r <= len(s2):
            test_dict = {}
            for letter in s2[l:r]:
                test_dict[letter] = 1 + test_dict.get(letter, 0)
            if s1_dict == test_dict:
                return True
            l += 1
            r += 1
        return False
                

