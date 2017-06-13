# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        counter = 0
        while(root != None or len(stack) != 0):
            if(root != None):
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                counter += 1
                if(counter == k):
                    return node.val
                root = node.right
        