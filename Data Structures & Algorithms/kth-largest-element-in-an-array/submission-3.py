class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        for i in range(k - 1):
            heapq.heappop(max_heap)

        return -1 * (max_heap[0])