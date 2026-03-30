# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, depth, rightSide):
            if not root:
                return
            
            if depth == len(rightSide):
                rightSide.append(root.val)
            
            dfs(root.right, depth + 1, rightSide)
            dfs(root.left, depth + 1, rightSide)
        
        rightSide = []
        dfs(root, 0, rightSide)
        return rightSide