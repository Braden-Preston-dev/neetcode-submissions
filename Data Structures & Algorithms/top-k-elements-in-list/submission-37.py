class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countK = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for i in nums:
            countK[i] = 1 + countK.get(i, 0)
        for num, freq in countK.items():
            frequency[freq].append(num)
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res



            

            