# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        node_list = []
        while(root != None or len(stack) != 0):
            if(root != None):
                stack.append(root)
                node_list.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        
        for i in xrange(len(node_list)):
            node_list[i].left = None
            if(i == len(node_list)-1):
                node_list[i].right = None
            else:
                node_list[i].right = node_list[i+1]