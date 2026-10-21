class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = []
        w, r = 0, 0
        
        while r < len(chars):
            chars[w] = chars[r]
            w += 1

            t = r + 1
            while t < len(chars) and chars[t] == chars[r]:
                t += 1
            
            if t - r > 1:
                for c in str(t - r):
                    chars[w] = c
                    w += 1
            r = t
        return w