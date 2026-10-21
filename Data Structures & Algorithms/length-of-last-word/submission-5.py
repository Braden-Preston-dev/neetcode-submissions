class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        r = len(s) - 1

        while s[r] == " ":
            r -= 1

        i = r
        while i >= 0 and s[i].isalpha():
            i -= 1
        return r - i