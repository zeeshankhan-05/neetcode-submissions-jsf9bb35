class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        waterTrapped = 0
        
        while left < right:
            # Move the left pointer if the height at left is smaller
            if height[left] < height[right]:
                # If the current height is smaller than the leftMax, calculate water trapped
                if height[left] < leftMax:
                    waterTrapped += leftMax - height[left]
                else:
                    # Update leftMax if the current height is larger
                    leftMax = height[left]
                left += 1
            # Move the right pointer if the height at right is smaller or equal
            else:
                # If the current height is smaller than the rightMax, calculate water trapped
                if height[right] < rightMax:
                    waterTrapped += rightMax - height[right]
                else:
                    # Update rightMax if the current height is larger
                    rightMax = height[right]
                right -= 1
        
        return waterTrapped