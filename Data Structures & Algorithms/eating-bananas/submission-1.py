class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        slowest_eating_speed = high

        while low <= high:
            k = (low + high) // 2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(float(pile) / k)
            if total_time <= h:
                slowest_eating_speed = k
                high = k - 1
            else:
                low = k + 1

        return slowest_eating_speed