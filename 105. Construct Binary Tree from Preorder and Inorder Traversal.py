# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        # print preorder
        # print inorder
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if(len(preorder) == 0 and len(inorder) == 0):
            return None
        if(len(preorder) == 1 and len(inorder) == 1):
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        root_idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+root_idx], inorder[0:root_idx])
        root.right = self.buildTree(preorder[1+root_idx:], inorder[root_idx+1:])
        return root