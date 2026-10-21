class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for l in range(len(nums) - 2):
            m = l + 1
            r = len(nums) - 1
            if nums[l] > 0: break
            if l > 0 and nums[l] == nums[l - 1]: continue

            while m < r:
                added = nums[r] + nums[l] + nums[m]

                if added == 0: 
                    
                    res.append([nums[l], nums[m], nums[r]])
                    r -= 1
                    m += 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1
                elif added > 0: r -= 1
                else: m += 1


        
        return res 