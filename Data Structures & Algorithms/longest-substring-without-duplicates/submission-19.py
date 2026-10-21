class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        seen = set()

        while r < len(s):
            while s[r] in seen and l < len(s):
                seen.remove(s[l])
                l += 1
                continue
            longest = max(r - l + 1, longest)
            seen.add(s[r])
            r += 1
        
        return longest