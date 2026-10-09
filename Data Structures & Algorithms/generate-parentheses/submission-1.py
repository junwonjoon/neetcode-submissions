class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        total_combinations = 2 ** (n * 2)
        lower_bound = 2 ** (n * 2 - 1)
        ans = []
        for i in range(lower_bound, total_combinations):
            binary_str = f"{i:0{n}b}"
            curr = ""
            validity = 0
            for b in binary_str:
                curr += "(" if b == "1" else ")"
                validity += 1 if b == "1" else -1
                if validity < 0 or abs(validity) > (len(binary_str) // 2 + 1):
                    break
            if validity == 0:
                ans.append(curr)
        return ans
