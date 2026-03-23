# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        ans=[0]
        def check(node, ans):
            if not node:
                return
            if node.val %2==0 and node.left :
                if node.left.left:
                    ans[0]+=node.left.left.val
                if node.left.right:
                    ans[0]+=node.left.right.val
            if node.val %2==0 and node.right:
                if node.right.left:
                    ans[0]+=node.right.left.val
                if node.right.right:
                    ans[0]+=node.right.right.val
                
            check(node.left, ans)
            check(node.right, ans)
        
        check(root, ans)
        return ans[0]