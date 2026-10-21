class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        l, r = 0, 0
        ans = []

        while l < len(heights):
            r = l + 1
            tallest = 0
            count = 0
            while r < len(heights):
                if min(heights[l], heights[r]) > tallest:
                    count += 1
                tallest = max(heights[r], tallest)
                r += 1
            ans.append(count)
            l += 1
        return ans