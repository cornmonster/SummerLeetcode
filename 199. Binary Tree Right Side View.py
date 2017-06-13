# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if(root == None):
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while(len(queue) != 0):
            queue_len = len(queue)
            res.append(queue[queue_len-1].val)
            for i in xrange(queue_len):
                temp = queue.popleft()
                if(temp.left != None):
                    queue.append(temp.left)
                if(temp.right != None):
                    queue.append(temp.right)
        return res
                