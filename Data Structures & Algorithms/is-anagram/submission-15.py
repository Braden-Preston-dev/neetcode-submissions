class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        if len(s) != len(t):
            return False
        
        for c1, c2 in zip(s, t):
            sCount[c1] = sCount.get(c1, 0) + 1
            tCount[c2] = tCount.get(c2, 0) + 1
        
        return sCount == tCount