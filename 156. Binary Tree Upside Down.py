# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if(root == None or root.left == None and root.right == None):
            return
        self.helper(root.left)
        self.helper(root.right)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return
        
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(root == None):
            return None
        new_root = root
        while(new_root.left != None):
            new_root = new_root.left
        self.helper(root)
        return new_root