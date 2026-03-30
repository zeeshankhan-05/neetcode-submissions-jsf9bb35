class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Enumerate through the list
        # For each number in the list, subtract that number from the target to get the difference
        # Check if that difference is in the map (mapping the index to the number)
        # If it is not, add that number to the list, marking its index position
        # If it is, return the index position of that difference and that number

        sum = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in sum:
                return [sum[diff], index]
                
            sum[num] = index