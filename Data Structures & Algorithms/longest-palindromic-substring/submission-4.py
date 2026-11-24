class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resIdx = resLen = 0
        cache = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or cache[i + 1][j - 1]):
                    cache[i][j] = True
                    if resLen < j - i + 1:
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx : resIdx + resLen]




