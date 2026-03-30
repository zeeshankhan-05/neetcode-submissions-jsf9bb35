class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hashmap that holds the diff value and its index position
        # Enumerate through the array to count the index position
        # Calculate the diff from the target and each number in the array
        # If diff is in the hashmap, return the index position of diff and i
        # If not, add the diff to the hashmap, mapping it to its index position

        map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in map:
                return [map[diff], i]
            map[n] = i