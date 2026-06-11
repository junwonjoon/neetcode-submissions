class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        complement = {"[": "]", "{" : "}", "(" : ")"}
        for bracket in s:
            if bracket in "[({":
                stack.append(complement[bracket])
            else:
                if len(stack) == 0 or bracket != stack.pop():
                    return False
        if stack:
            return False
        return True
        
