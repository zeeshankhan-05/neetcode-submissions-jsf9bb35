class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        min_len = float('inf')

        for i in range(n):
            required_sum = target + prefix[i]
            low, high = i + 1, n
            while low <= high:
                mid = (low + high) // 2
                if prefix[mid] >= required_sum:
                    high = mid - 1
                else:
                    low = mid + 1

            if low <= n:
                min_len = min(min_len, low - i)

        return min_len if min_len != float('inf') else 0