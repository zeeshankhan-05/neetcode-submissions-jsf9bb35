class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        more_than_once = set()

        for num in nums:
            if num in more_than_once:
                return True
            more_than_once.add(num)

        return False