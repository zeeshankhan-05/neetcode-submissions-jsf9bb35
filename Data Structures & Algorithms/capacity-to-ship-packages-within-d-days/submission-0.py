class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def can_ship(capacity):
            days_needed = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = 0

                current_weight += weight

                if days_needed > days:
                    return False

            return True

        while left < right:
            mid = left + (right - left) // 2

            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left
