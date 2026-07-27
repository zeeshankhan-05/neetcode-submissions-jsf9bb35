class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums[i] == nums[j]
        # abs(i - j) <= k

        dupes = {}

        for i in range(len(nums)):
            if nums[i] in dupes and i - dupes[nums[i]] <= k:
                return True
            
            dupes[nums[i]] = i
        
        return False

        # [1, 2, 3, 1], k = 3
        # [0, 1, 2, 3]

        # [2, 1, 2], k = 1
        # [0, 1, 2]

        # size of the fixed sliding window
