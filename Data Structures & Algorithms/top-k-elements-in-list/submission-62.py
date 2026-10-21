class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        frequency = defaultdict(list)

        for val, freq in count.items():
            frequency[freq].append(val)
        res = []

        for i in range(len(nums), 0, -1):
            while frequency.get(i):
                res.append(frequency[i].pop())
                if len(res) == k:
                    return res
                
        return res