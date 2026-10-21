class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curWindow = set()
        maxLength = 0
        for c in s:
            while c in curWindow:
                curWindow.remove(s[l])
                l += 1
            curWindow.add(c)

            maxLength = max(maxLength, len(curWindow))
        
        return maxLength