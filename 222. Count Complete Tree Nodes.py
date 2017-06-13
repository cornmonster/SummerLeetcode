# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if(root == None):
            return -1
        return 1 + self.helper(root.left)
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        h = self.helper(root)
        while(root != None):
            if(self.helper(root.right) == h-1):
                res += 2 ** h
                root = root.right
            else:
                res += 2 ** (h-1)
                root = root.left
            h -= 1
        return res