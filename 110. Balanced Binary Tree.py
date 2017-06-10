# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, nodes):
        if(root == None):
            return 0
        if(root.left == None and root.right == None):
            nodes[root] = (0, 0)
            return 1
            
        left = self.helper(root.left, nodes)
        right = self.helper(root.right, nodes)
        
        nodes[root] = (left, right)
        return max(left, right) + 1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = dict()
        self.helper(root, nodes)
        # print nodes
        for key in nodes.keys():
            if(abs(nodes[key][0] - nodes[key][1]) > 1):
                return False
        
        return True