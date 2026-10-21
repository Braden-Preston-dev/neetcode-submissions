class Solution:
    def largestGoodInteger(self, num: str) -> str:

        l, r = 0, 0
        res = "0"
        while r < len(num):
            if num[r] == num[l]:
                if r - l >= 2: 
                    res = max(res, (num[r] * 3))
                r += 1
            else: l = r

        return str(res) if res != "0" else ""