class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while True:
            n = self.squareDigits(n)
            print(n)
            if n == 1: return True
            if n in seen: break
            seen.add(n)
        return False

    def squareDigits(self, n):
        res = 0
        for i in str(n):
            res += int(i) ** 2
        return res