class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calcDistance(points):
            return [math.sqrt(points[0] ** 2 + points[1] ** 2), points]

        maxHeap = []
        heapq.heapify(maxHeap)

        for point in points:
            distance = calcDistance(point)

            heapq.heappush(maxHeap, (-1 * distance[0], distance[1]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        values = [value for _, value in maxHeap]
        return values