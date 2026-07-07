class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 4, 5, 6
        # 6, 5, 4
        # 0, 1, 2
        pairs = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in pairs:
                return [pairs[diff], i]

            pairs[num] = i