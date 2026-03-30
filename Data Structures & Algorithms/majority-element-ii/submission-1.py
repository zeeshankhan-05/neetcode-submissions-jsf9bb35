class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        req = math.floor(n / 3)
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ele = []
        for num, count in freq.items():
            if count > req:
                ele.append(num)

        return ele