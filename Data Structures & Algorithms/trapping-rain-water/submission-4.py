class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        water = 0

        while l < r:
            if lmax < rmax:
                l += 1
                if height[l] > lmax: lmax = height[l]
                else: water += lmax - height[l]
            else:
                r -= 1
                if height[r] > rmax: rmax = height[r]
                else: water += rmax - height[r]

        return water
            

