class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def valid_or_not(paren:str) -> bool:
            valid = 0
            for letter in paren:
                if valid < 0:
                    return False
                if letter == "(":
                    valid += 1
                elif letter == ")":
                    valid -= 1
            if valid == 0:
                return True
            else:
                return False
        total_combinations = 2 ** (n * 2)
        lower_bound = 2 ** (n * 2 - 1)
        ans = []
        for i in range(lower_bound, total_combinations):
            binary_str = f"{i:0{n}b}"
            curr = ""
            for b in binary_str:
                curr += "(" if b == "1" else ")"
            if valid_or_not(curr):
                ans.append(curr)
        return ans
