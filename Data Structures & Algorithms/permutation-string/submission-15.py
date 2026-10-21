class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False

        r = len(s1)
        count = Counter(s1)
        window = Counter(s2[ : len(s1)])

        if window == count:
            return True

        while r < len(s2):
            window[s2[r]] += 1

            leftChar = s2[r - len(s1)]
            window[leftChar] -= 1

            if window[leftChar] == 0:  del window[leftChar]
            if count == window: return True

            r += 1

            
        return False