class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        skip = 0

        for l in range(len(nums) - 2):
            m = l + 1
            r = len(nums) - 1

            while m < r:
                added = nums[r] + nums[l] + nums[m]

                if added == 0: 
                    res.add(tuple([nums[l], nums[m], nums[r]]))
                    r -= 1
                    m += 1
                elif added > 0: r -= 1
                else: m += 1
        
        return list(res) 