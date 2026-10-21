class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for str in strs:
            letters = [0] * 26
            for char in str:
                letters[ord(char) - ord('a')] += 1
            res[tuple(letters)].append(str)
        return list(res.values())
                