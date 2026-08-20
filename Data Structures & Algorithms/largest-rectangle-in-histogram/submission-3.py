class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start_index, height)
        largest = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, previous_height = stack.pop()

                width = i - index
                area = previous_height * width
                largest = max(largest, area)

                start = index

            stack.append((start, height))

        # Rectangles still in the stack can extend to the end
        n = len(heights)

        for index, height in stack:
            width = n - index
            area = height * width
            largest = max(largest, area)

        return largest