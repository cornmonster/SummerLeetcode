# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recursive solution
        # if(root == None):
        #     return 0
        # if(root.left == None and root.right == None):
        #     return root.val
        
        # rob_this = root.val
        # if(root.left != None):
        #     rob_this += self.rob(root.left.left) + self.rob(root.left.right)
        # if(root.right):
        #     rob_this += self.rob(root.right.left) + self.rob(root.right.right)
        
        # not_rob_this = self.rob(root.left) + self.rob(root.right)
        
        # return max(rob_this, not_rob_this)

        # iterative solution
        if(root == None):
            return 0
        layers = []
        queue = collections.deque()
        queue.append(root)
        node_to_opt = dict()
        node_to_opt[None] = 0
        while(len(queue) != 0):
            layer_length = len(queue)
            layers.append([])
            for i in xrange(layer_length):
                layers[len(layers)-1].append(queue[i])
            for i in xrange(layer_length):
                temp = queue.popleft()
                if(temp.left != None):
                    queue.append(temp.left)
                if(temp.right != None):
                    queue.append(temp.right)
        
        for i in xrange(len(layers)):
            layer_to_access = len(layers)-1-i
            for node in layers[layer_to_access]:
                if(node.left == None and node.right == None):
                    node_to_opt[node] = node.val
                else:
                    rob_this = node.val
                    if(node.left != None):
                        rob_this += node_to_opt[node.left.left] + node_to_opt[node.left.right]
                    if(node.right != None):
                        rob_this += node_to_opt[node.right.left] + node_to_opt[node.right.right]
                    
                    not_rob_this = node_to_opt[node.left] + node_to_opt[node.right]
                    node_to_opt[node] = max(rob_this, not_rob_this)
        
        return node_to_opt[root]