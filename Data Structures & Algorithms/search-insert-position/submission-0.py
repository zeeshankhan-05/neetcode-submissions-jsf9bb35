class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        insert_index = len(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                insert_index = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return insert_index