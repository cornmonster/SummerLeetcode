# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, s, res):
        new_str = s + '->' + str(root.val)
        if(root.left == None and root.right == None):
            res.append(new_str)
            return
        if(root.left != None):
            self.helper(root.left, new_str, res)
        if(root.right != None):
            self.helper(root.right, new_str, res)


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if(root == None):
            return []

        res_left = []
        res_right = []
        if(root.left != None):
            self.helper(root.left, str(root.val), res_left)
        if(root.right != None):
            self.helper(root.right, str(root.val), res_right)
        if(root.left == None and root.right == None):
            return [str(root.val)]
        
        return res_left + res_right