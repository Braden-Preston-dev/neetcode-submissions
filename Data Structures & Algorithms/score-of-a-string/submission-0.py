class Solution:
    def scoreOfString(self, s: str) -> int:
        
        i = 0
        sums = 0

        while i + 1 < len(s):
            sums += abs(ord(s[i]) - ord(s[i + 1]))
            i += 1
        return sums