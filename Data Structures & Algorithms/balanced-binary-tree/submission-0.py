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

            leftBalanced, leftHeight = dfs(root.left)
            rightBalanced, rightHeight = dfs(root.right)
            
            if not leftBalanced:
                return False, 0
            
            if not rightBalanced:
                return False, 0

            if abs(leftHeight - rightHeight) > 1:
                return False, 0

            return True, 1 + max(leftHeight, rightHeight)

        balanced, _ = dfs(root)
        return balanced