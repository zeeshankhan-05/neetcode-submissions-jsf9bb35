class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        water_container = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            water_container = max(water_container, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return water_container