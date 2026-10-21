from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        ana = defaultdict(list)

        for s in strs:
            a = [0] * 26

            for c in s:
                a[ord(c) - ord('a')] += 1
            ana[tuple(a)].append(s)


        return list(ana.values())