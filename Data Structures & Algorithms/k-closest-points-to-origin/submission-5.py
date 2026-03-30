class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            x, y = point
            distance = math.sqrt(x ** 2 + y ** 2)

            heapq.heappush(maxHeap, (-distance, point))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        closestPoints = []
        for _, point in maxHeap:
            closestPoints.append(point)

        return closestPoints