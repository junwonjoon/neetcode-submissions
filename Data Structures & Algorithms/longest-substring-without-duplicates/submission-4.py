class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str = ""
        count = 0
        for letter in s:
            if letter.lower() not in max_str:
                max_str += letter.lower()
            else:
                max_str = max_str[max_str.index(letter.lower()) + 1:] + letter
                print(max_str)
            count = max(count, len(max_str))
        return count