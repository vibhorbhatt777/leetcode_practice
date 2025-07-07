# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0
        def solve(node):
            if node == None:
                return 0
            lh = solve(node.left)
            rh = solve(node.right)
            self.diameter = max(self.diameter,lh+rh)
            return 1 + max(lh,rh)
        
        solve(root)
        return self.diameter
        