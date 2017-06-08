# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(root == None):
            return root
        # the alg. is: for each node, switch its left child and right child
        stack = []
        stack.append(root)
        while(len(stack) != None):
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if(node.left != None):
                stack.append(node.left)
            if(node.right != None):
                stack.append(node.right)
        return root