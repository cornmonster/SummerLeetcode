# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        last_visited = None
        while(root != None or len(stack) != 0):
            if(root != None):
                stack.append(root)
                root = root.left
            else:
                temp = stack[len(stack)-1]
                if(temp.right != None and last_visited != temp.right):
                    root = temp.right
                else:
                    res.append(temp.val)
                    last_visited = stack.pop()
        return res