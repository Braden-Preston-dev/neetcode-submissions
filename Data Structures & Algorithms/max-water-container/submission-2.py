class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        a = 0
        maxArea = 0
        while l < r:
            if heights[l] > heights[r]:
                a = (r - l)* heights[r]
                r -= 1
            
            elif heights[r] > heights[l]:
                a = (r - l)* heights[l]
                l += 1
            else:
                a = (r - l)* heights[l]
                if heights[l + 1] > heights[r - 1]:
                    l += 1
                else:
                    r -= 1
            maxArea = max(a, maxArea)
        
        return maxArea