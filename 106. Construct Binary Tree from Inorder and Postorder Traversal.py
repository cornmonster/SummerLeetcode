# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if(len(inorder) == 0 and len(postorder) == 0):
            return None
        elif(len(inorder) == 1 and len(postorder) == 1):
            return TreeNode(inorder[0])
        
        root = TreeNode(postorder[len(postorder)-1])
        left_inorder = inorder[0:inorder.index(root.val)]
        right_inorder = inorder[inorder.index(root.val)+1:]
        left_postorder = postorder[0:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder)-1]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root