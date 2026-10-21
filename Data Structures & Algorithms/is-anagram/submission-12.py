class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sVal = {}
        tVal = {}

        if (len(s) != len(t)):
            return False

        for i in range(0, len(s)):
            sVal[s[i]] = sVal.get(s[i], 0) + 1
            tVal[t[i]] = tVal.get(t[i], 0) + 1
        return sVal == tVal
        