class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = { "2" : "abc", "3": "def", "4" : "ghi", "5" : "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        stack = [combinations[x] for x in digits[::-1]]
        if not digits:
            return []
        lst = list(stack[-1])
        stack.pop()
        while stack:
            lst_temp = []
            for comb in stack.pop():
                for prev_comb in lst:
                    for letter in comb:
                        lst_temp.append(prev_comb + letter)
            lst = lst_temp.copy()
        return lst