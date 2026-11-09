class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashed = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in hashed:
                m = n
                while m in hashed:
                    m += 1
                longest = max(longest, m - n)
                n = m

        return longest