# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        queue = collections.deque()
        queue.append(root)
        counter = 0
        while(len(queue) != None):
            counter += 1
            queue_len = len(queue)
            for i in xrange(queue_len):
                temp = queue.popleft()
                if(temp.left == None and temp.right == None):
                    return counter
                if(temp.left != None):
                    queue.append(temp.left)
                if(temp.right != None):
                    queue.append(temp.right)
        