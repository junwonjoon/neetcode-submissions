class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = { "2" : "abc", "3": "def", "4" : "ghi", "5" : "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        lst = list(combinations[digits[0]])
        for digit in digits[1:]:
            new_comb = []
            for letter in combinations[digit]:
                for prev_comb in lst:
                    new_comb.append(prev_comb + letter)
            lst = new_comb.copy()
        return lst