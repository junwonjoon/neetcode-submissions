class Solution:
    def isValid(self, s: str) -> bool:
        len_s = len(s)
        if len_s % 2 == 1:
            return False
        stack = []
        i = 0
        while i < len_s:
            if s[i] in "[({":
                stack.append(self.complement(s[i]))
            else:
                if len(stack) == 0 or s[i] != stack.pop():
                    return False
            i += 1
        if stack:
            return False
        else:
            return True
        
    def complement(self, s: str) -> str:
        if s in "()":
            if s == "(":
                return ")"
            else:
                return "("
        elif s in "[]":
            if s == "[":
                return "]"
            else:
                return "["
        elif s in "{}":
            if s == "{":
                return "}"
            else:
                return "{"
        else:
            return ""
