# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # recursive solution
        # if not root or not p or not q:
        #     return None
        # if (max(p.val, q.val) < root.val):
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif (min(p.val, q.val) > root.val):
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root

        # iterative solution
        if(root == None or p == None or q == None):
            return None
        while(root.val > max(p.val, q.val) or root.val < min(p.val, q.val)):
            if(root.val > max(p.val, q.val)):
                root = root.left
            else:
                root = root.right
        return root