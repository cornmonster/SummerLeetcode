# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        queue.append(root)
        res = []
        while(len(queue) != 0):
            length = len(queue)
            buf = []
            for i in xrange(length):
                temp = queue.popleft()
                buf.append(temp.val)
                if(temp.left != None):
                    queue.append(temp.left)
                if(temp.right != None):
                    queue.append(temp.right)
            res.append(buf)
        return res