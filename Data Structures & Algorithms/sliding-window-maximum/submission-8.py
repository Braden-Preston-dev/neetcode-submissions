class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        maxHeap = []

        for r in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[r], r))
            
            if r >= k - 1:
                while maxHeap and maxHeap[0][1] <= r - k: heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
        
        return res
