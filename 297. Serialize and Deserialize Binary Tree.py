# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque()
        res = []
        queue.append(root)
        while(len(queue) != 0):
            temp = queue.popleft()
            if(temp != None):
                res.append(temp.val)
                queue.append(temp.left)
                queue.append(temp.right)
            else:
                res.append(temp)
        return ','.join([str(x) for x in res])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = []
        data = data.split(',')
        for s in data:
            if(s != 'None'):
                values.append(int(s))
            else:
                values.append(None)
        
        if(values[0] == None):
            return None
        
        root = TreeNode(values[0])
        values_idx = 1
        queue = collections.deque()
        queue.append(root)
        while(len(queue) != 0 and values_idx < len(values)):
            temp = queue.popleft()
            if(values[values_idx] != None):
                temp.left = TreeNode(values[values_idx])
                queue.append(temp.left)
            values_idx += 1
            if(values[values_idx] != None):
                temp.right = TreeNode(values[values_idx])
                queue.append(temp.right)
            values_idx += 1
            
        return root
        
            
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))