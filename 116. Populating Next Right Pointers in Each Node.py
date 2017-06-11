# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
import collections
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if(root == None):
            return
        queue = collections.deque()
        queue.append(root)
        while(len(queue) != 0):
            temp_len = len(queue)
            for i in xrange(temp_len):
                if(i == temp_len-1):
                    queue[i].next = None
                else:
                    queue[i].next = queue[i+1]
            for i in xrange(temp_len):
                temp_node = queue.popleft()
                if(temp_node.left != None):
                    queue.append(temp_node.left)
                if(temp_node.right != None):
                    queue.append(temp_node.right)