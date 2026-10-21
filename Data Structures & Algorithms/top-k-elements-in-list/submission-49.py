class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Declare variable
        res = []
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # Counts the frquency for each element
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Populates a frequency table
        for num, frequency in count.items():
            freq[frequency].append(num)
        
        
        for i in range(len(nums), -1, -1):
            if freq[i] is not None:
                for j in freq[i]:
                    if len(res) == k:
                        return res
                    res.append(j)
        return res