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

        # [1, 2, 4, 6]
        # [1, 2, 8, 48] - prefix product
        # [48, 24, 12, 8] - output

        # How do I get the product of all the other numbers for each element?