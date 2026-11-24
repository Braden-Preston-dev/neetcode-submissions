class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cache = [-1] * len(s)

        def dfs(i):
            if i == len(s): return True
            if cache[i] != -1: return cache[i]

            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i : i + len(word)]:
                    cache[i] = dfs(i + len(word))
                    if cache[i]: return True
            cache[i] = False
            return False

        return dfs(0)