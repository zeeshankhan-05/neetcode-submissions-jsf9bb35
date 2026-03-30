class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1. Calculate floor(n / 3)
        # 2. Create a hashmap that maps the each unique integer to their frequency
        # 3. Return the integers that have a frequency > floor(n / 3)

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