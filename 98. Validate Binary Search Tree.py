# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, max_val, min_val, root):
        if(root == None):
            return True
        if(root.val >= max_val or root.val <= min_val):
            return False
        else:
            return self.helper(root.val, min_val, root.left) and self.helper(max_val, root.val, root.right)
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None):
            return True
        return self.helper(float('inf'), -float('inf'), root)