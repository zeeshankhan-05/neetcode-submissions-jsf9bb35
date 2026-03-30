import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distancesFromOrigin = []

        for point in points:
            x, y = point
            distance = math.sqrt(x**2 + y**2)
            distancesFromOrigin.append((distance, point))

        distancesFromOrigin.sort()

        closestPoints = []
        for i in range(k):
            closestPoints.append(distancesFromOrigin[i][1])

        return closestPoints
