class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_t = list(t)
        for letter in s:
            if len(s) == len(t) and letter in list_t:
                list_t.remove(letter)
            else:
                return False
        return True
            
            
    