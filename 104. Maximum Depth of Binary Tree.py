# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        # bfs solution
        # queue = collections.deque()
        # queue.append(root)
        # res = 0
        # while(len(queue) != 0):
        #     res += 1
        #     temp_len = len(queue)
        #     for i in xrange(temp_len):
        #         node = queue.popleft()
        #         if(node.left != None):
        #             queue.append(node.left)
        #         if(node.right != None):
        #             queue.append(node.right)
        
        # return res

        # dfs Solution
        node_stack = []
        stack.append((root，1))
        res = 1
        while(len(stack) != 0):
            node, depth = stack.pop()
            if(depth > res):
                res = depth
            if(node.left != None):
                stack.append((node.left, depth+1))
            if(node.right != None):
                stack.append((node.right, depth+1))
        return res
            

