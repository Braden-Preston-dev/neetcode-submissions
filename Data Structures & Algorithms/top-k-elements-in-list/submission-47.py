class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # declare variable
        res = []
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # place elements in buckets
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for key, val in count.items():
            freq[val].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for i in freq[i]:
                res.append(i)
                if k == len(res):
                    return res
        return res
            