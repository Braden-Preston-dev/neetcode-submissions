class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, a in enumerate(nums):

            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[r] + nums[l]
                if threeSum == 0:
                    res.append([a, nums[r], nums[l]])
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        return res