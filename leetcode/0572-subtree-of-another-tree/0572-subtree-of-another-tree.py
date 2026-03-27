# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(node):
            if same(node, subRoot):
                return True
            if not node:
                return False

            return check(node.left) or check(node.right)

        
        def same(n1, n2):
            if not n1 or not n2:
                return n1==n2
            if n1.val!=n2.val:
                return False
            
            return same(n1.left, n2.left) and same(n1.right, n2.right)

        return check(root)


        