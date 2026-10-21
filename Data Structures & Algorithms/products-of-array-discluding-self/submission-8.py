class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        prefix = [1] * len(nums)
        pre = 1
        for i in range(1, len(nums)):
            pre *= nums[i - 1]
            prefix[i] = pre

        suf = 1
        suffix = [1] * len(nums)
        for j in range(len(nums) - 2, -1, -1):
            suf *= nums[j + 1]
            suffix[j] = suf
        for k in range(len(nums)):
            output[k] = prefix[k] * suffix[k]

        return output

