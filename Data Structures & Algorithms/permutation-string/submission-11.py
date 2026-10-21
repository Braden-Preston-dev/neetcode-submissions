class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False

        l, r = 0, len(s1) - 1
        count = Counter(s1)

        while r < len(s2):
            
            if count == Counter(s2[l : r + 1]): return True
            
            r += 1
            l += 1

        return False