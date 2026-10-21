class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        w1, w2 = 0, 0
        l1, l2 = len(word1), len(word2)

        while w1 < l1 or w2 < l2:
            if w1 < l1:
                res.append(word1[w1])
            if w2 < l2:
                res.append(word2[w2])
            w1 += 1
            w2 += 1

        return "".join(res)