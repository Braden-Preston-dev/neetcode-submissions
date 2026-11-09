class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        cur = {}
        l = r = 0
        longest = 1

        while r < len(s):
            if s[r] in cur: l = max(cur[s[r]] + 1, l)
            longest = max(longest, r - l + 1)
            cur[s[r]] = r
            r += 1
    
        return longest