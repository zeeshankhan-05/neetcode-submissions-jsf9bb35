class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        slowestEatingSpeed = high

        while low <= high:
            k = low + ((high - low) // 2)

            totalTime = 0
            for bananas in piles:
                totalTime += math.ceil(float(bananas) / k)
            if totalTime <= h:
                slowestEatingSpeed = k
                high = k - 1
            else:
                low = k + 1

        return slowestEatingSpeed