# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursive solution
    # def isSameTree(self, p, q):
    #     """
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: bool
    #     """
    #     if(p == None and q != None or p != None and q == None):
    #         return False
    #     if(p == None and q == None):
    #         return True
    #     elif(p.val != q.val):
    #         return False

    #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    # dfs solution
    def isSameTree(self, p, q):
        stack = []
        while(p != None or q != None or len(stack) != 0):
            if(p != None and q != None):
                if(p.val != q.val):
                    return False
                stack.append((p, q))
                p = p.left
                q = q.left
            elif(p != None and q == None or p == None and q != None):
                return False
            else:
                p, q = stack.pop()
                if(p.val != q.val):
                    return False
                p = p.right
                q = q.right
        return True