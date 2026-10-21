class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = len(nums) // 2
        freq = {}

        for i in nums:

            freq[i] = 1 + freq.get(i, 0)

            if freq[i] > majority: return i
        return 0

