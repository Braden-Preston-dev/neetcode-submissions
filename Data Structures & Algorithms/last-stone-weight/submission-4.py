class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            heaviest = heapq.heappop(max_heap)

            if len(max_heap) > 1:
                heapq.heappush(max_heap, heaviest - heapq.heappop(max_heap))
            else: max_heap[0] = heaviest - max_heap[0]
        return abs(max_heap[0])