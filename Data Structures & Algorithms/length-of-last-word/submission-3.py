class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        r = len(s) - 1
        i = r
        seen = False

        for i in range(len(s) - 1, 0, -1):
            r = i
            while s[i].isalpha():
                i -= 1
                seen = True
            if seen: break
        return r - i if r - i else 1