class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        longest = 0
        cur = {}

        for r in range(len(s)):
            if s[r] in cur and cur[s[r]] >= l:
                l = cur[s[r]] + 1
            cur[s[r]] = r
            longest = max(r - l + 1, longest)

        return longest
            