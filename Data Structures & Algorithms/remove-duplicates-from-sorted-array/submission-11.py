class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        uniqueIndex = 1
        l, r = 0, 1

        while r < len(nums):
            if nums[l] != nums[r]:
                nums[uniqueIndex] = nums[r]
                uniqueIndex += 1
                l = r
            r += 1
        return uniqueIndex
