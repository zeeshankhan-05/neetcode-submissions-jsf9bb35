# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
    
        def helper(pre_start, in_start, in_end):
            if pre_start >= len(preorder) or in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            root_index_in_inorder = inorder_index_map[root_val]
            
            left_subtree_size = root_index_in_inorder - in_start
            
            root.left = helper(pre_start + 1, in_start, root_index_in_inorder - 1)
            root.right = helper(pre_start + 1 + left_subtree_size, root_index_in_inorder + 1, in_end)
            
            return root
        
        return helper(0, 0, len(inorder) - 1)