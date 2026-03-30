class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupes = set()

        for i in range(len(nums)):
            if nums[i] in dupes:
                return True
            dupes.add(nums[i])
            if len(dupes) > k:
                dupes.remove(nums[i - k])
        return False