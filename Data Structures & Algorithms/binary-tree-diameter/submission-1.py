# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter = 0
        def longestpathtoleaf(root: Optional[TreeNode]):
            nonlocal maxdiameter
            if root.right:
                rightpath = 1 + longestpathtoleaf(root.right)
            else:
                rightpath = 0
            if root.left:
                leftpath = 1 + longestpathtoleaf(root.left)
            else:
                leftpath = 0
            maxdiameter = max(leftpath+rightpath, maxdiameter)
            return max(leftpath,rightpath)
        
        longestpathtoleaf(root)
        return maxdiameter

        



        