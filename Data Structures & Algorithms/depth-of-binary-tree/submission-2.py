# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        sk = [(root,1)]
        
        maxD = 0
        while sk:
            node, d = sk.pop()

            
            if node:
                maxD = max(d, maxD)

                sk.append((node.left,d + 1))
                sk.append((node.right, d + 1))
    
        
        return maxD


        