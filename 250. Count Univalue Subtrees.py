# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if(root == None):
            return (0, None)
        if(root.left == None and root.right == None):
            return (1, root.val)
        
        lcount, lval = self.helper(root.left)
        rcount, rval = self.helper(root.right)
        
        if(root.left != None and root.right == None and root.val == lval
            or root.left == None and root.right != None and root.val == rval
            or root.val == lval and root.val == rval):
            return (lcount+rcount+1, root.val)
        else:
            return (lcount+rcount, None)
        
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]
        