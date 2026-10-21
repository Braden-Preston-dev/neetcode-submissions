class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        minHeap = [[value, key] for key, value in count.items()]
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)

        res = [i[1] for i in minHeap]
        return res