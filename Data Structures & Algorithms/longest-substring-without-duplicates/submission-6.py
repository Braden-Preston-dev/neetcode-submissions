class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLength = 0
        curr = set()

        while r < len(s):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1

            length = r - l + 1
            maxLength = max(length, maxLength)
            
            curr.add(s[r])
            r += 1    
        return maxLength