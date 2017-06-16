# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root == None):
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while(len(queue) != 0):
            queue_len = len(queue)
            cur_layer = []
            for i in xrange(queue_len):
                cur_layer.append(queue[i].val)
            for i in xrange(queue_len):
                temp = queue.popleft()
                if(temp.left != None):
                    queue.append(temp.left)
                if(temp.right != None):
                    queue.append(temp.right)
        return res.reverse()
                