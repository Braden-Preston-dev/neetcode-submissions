class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        p = 1
        for i in range(len(nums)):
            prefix[i] = p
            p *= nums[i]
        
        postfix = [1] * len(nums)
        s = 1
        for j in range(len(nums) - 1, -1, -1):
            postfix[j] = s
            s *= nums[j]
        res = []
        for k in range(len(nums)):
            res.append(postfix[k] * prefix[k])
            
        return res

