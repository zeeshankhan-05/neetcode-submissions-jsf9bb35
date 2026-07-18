class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            x, y = point
            distance = math.sqrt(x ** 2 + y ** 2)

            heapq.heappush_max(max_heap, (distance, point))

            if len(max_heap) > k:
                heapq.heappop_max(max_heap)

        closest_points = []
        
        for _, point in max_heap:
            closest_points.append(point)

        return closest_points