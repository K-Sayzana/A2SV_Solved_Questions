# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
    

        def check(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            if not node.left:
                return 1 + check(node.right)
            if not node.right:
                return 1 + check(node.left)
        
            return 1 + min(check(node.left), check(node.right))
        
        return check(root)

        return check(root)