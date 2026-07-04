class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        # 0, 1, 2
        # 4, 5, 6
        
        # 0 - 4
        # 1 5

        for i, num in enumerate(nums):
            diff = target - num

            if diff in pairs:
                return [pairs[diff], i]
            
            pairs[num] = i