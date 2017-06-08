# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self._helper(self.root)
        
    def _helper(self, root):
        while(root is not None):
            self.stack.append(root)
            root = root.left
            
    def hasNext(self):
        """
        :rtype: bool
        """
        if(len(self.stack) != 0):
            return True
        return False
        
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self._helper(node.right)
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())