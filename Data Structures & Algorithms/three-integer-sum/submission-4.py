class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total_sum = num + nums[left] + nums[right]
                if total_sum > 0:
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    triplet.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return triplet
