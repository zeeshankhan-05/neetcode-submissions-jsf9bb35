class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        output = [1] * len(nums)
        # [1, 1, 2, 1]

        prefix_prod = 1
        for i in range(len(nums)):
            output[i] = prefix_prod
            prefix_prod *= nums[i]
            # [1, 1, 2, 8]

        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            # [48, 24, 12, 8]
            output[i] *= suffix_prod
            suffix_prod *= nums[i] 

# [48, 24, 12, 8]
        return output