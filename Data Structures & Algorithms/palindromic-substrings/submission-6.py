class Solution:
    def countSubstrings(self, s: str) -> int:
        
        palindromes = 0

        cache = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or cache[i + 1][j - 1]):
                    cache[i][j] = True
                    palindromes += 1
        return palindromes