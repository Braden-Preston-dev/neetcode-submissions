class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        count = Counter(s)
        res = []

        last = {}
        for i, c in enumerate(s):
            last[c] = i

        l = 0
        curLast = 0
        for r in range(len(s)):
            curLast = max(curLast, last[s[r]])
            if curLast == r:
                res.append(r - l + 1)
                l = r + 1
        
        return res

