class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)

        prefixProduct = 1
        for n in range(len(nums)):
            product[n] = prefixProduct
            prefixProduct *= nums[n]

        postProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= postProduct
            postProduct *= nums[i]

        return product
        