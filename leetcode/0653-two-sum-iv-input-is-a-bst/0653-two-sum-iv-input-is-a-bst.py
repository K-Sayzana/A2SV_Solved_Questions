# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals=set()

        def trav(node):
            if not node:
                return False
            if (k-node.val) in vals:
                return True
            vals.add(node.val)
            
            return trav(node.left) or trav(node.right)
        
        return trav(root)