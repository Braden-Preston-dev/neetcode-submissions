class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        maxLength = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1

                while num + 1 in nums:
                    length += 1
                    num += 1
                maxLength = max(length, maxLength)

        return maxLength