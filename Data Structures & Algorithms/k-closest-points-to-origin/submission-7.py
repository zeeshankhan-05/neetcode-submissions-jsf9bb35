class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_distances = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            points_distances.append([dist, x, y])

        heapq.heapify(points_distances)
        closest_k_points = []

        while k > 0:
            dist, x, y = heapq.heappop(points_distances)
            closest_k_points.append([x, y])
            k -= 1

        return closest_k_points