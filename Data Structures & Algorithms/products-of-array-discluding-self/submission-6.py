class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        suffix = 1

        # Prefix product
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        # Suffix product
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output