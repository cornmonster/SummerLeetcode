# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, p, q):
        if(p == None and q == None):
            return True
        elif(p == None and q != None or p != None and q == None):
            return False
        elif(p.val != q.val):
            return False
        else:
            return self.helper(p.left, q.right) and self.helper(p.right, q.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # my solution
        if(root == None):
            return True
        return self.helper(root.left, root.right)
        
