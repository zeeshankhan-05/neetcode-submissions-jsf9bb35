class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [1, 2, 2, 2], target = 4
        # 1. Create a pointer at both ends
        # 2. Check if that those pointer values add up to the target
        # 3. Compare the sum against the target
        # If the sum is greater than the target, decrement the right pointer
        # Elif increment the left pointer
        # 4. Continue until the sum is equal to the target, returning the indices

        left, right, = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]