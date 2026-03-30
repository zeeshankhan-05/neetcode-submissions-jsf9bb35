# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levelOrderTraversal = []
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            levelValues = []
            
            for i in range(levelSize):
                node = queue.popleft()
                levelValues.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levelOrderTraversal.append(levelValues)
        
        return levelOrderTraversal