# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0

            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)

            if not left_balanced:
                return False, 0

            if not right_balanced:
                return False, 0

            if abs(left_height - right_height) > 1:
                return False, 0

            return True, 1 + max(left_height, right_height)

        balanced, _ = dfs(root)
        return balanced