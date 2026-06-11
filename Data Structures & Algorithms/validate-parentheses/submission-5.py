class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        for bracket in s:
            if bracket in "[({":
                stack.append(self.complement(bracket))
            else:
                if len(stack) == 0 or bracket != stack.pop():
                    return False
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
