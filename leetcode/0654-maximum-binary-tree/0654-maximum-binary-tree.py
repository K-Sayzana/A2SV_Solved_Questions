# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def solve(arr):
            if len(arr)==0:
                return None

            idx=arr.index(max(arr))
            node =TreeNode(arr[idx])
            node.left=solve(arr[:idx])
            node.right=solve(arr[idx+1:])

            return node
        

        return solve(nums)