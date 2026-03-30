class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()

        for i in nums:
            if i in dupes:
                return True
            dupes.add(i)
        return False