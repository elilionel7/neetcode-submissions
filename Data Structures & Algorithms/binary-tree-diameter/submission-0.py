# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        lh =  self.maxH(root.left)
        rh =  self.maxH(root.right)
        dia = lh + rh

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(dia, sub)
    
    def maxH(self, root):
        if not root: return 0

        return 1 + max(self.maxH(root.left), self.maxH(root.right))
        