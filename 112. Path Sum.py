# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isLeaf(self, root):
        return root != None and root.left == None and root.right == None
        
    def helper(self, root, sum):
        if(self.isLeaf(root) and sum == root.val):
            return True
        if(self.isLeaf(root) and sum != root.val):
            return False
        
        if(root.left != None and root.right != None):
            return self.helper(root.left, sum-root.val) or self.helper(root.right, sum-root.val)
        elif(root.left == None and root.right != None):
            return self.helper(root.right, sum-root.val)
        elif(root.left != None and root.right == None):
            return self.helper(root.left, sum-root.val)
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if(root == None):
            return False
        return self.helper(root, sum)