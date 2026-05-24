class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        if len(s) == 1:
            return True
        r_i = 1
        i = 0
        while i <= len(s)//2 and r_i <= len(s)//2 + 1:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[-r_i].isalnum():
                r_i += 1
                continue
            if s[i].lower() != s[-r_i].lower():
                return False
            i += 1
            r_i += 1
        return True