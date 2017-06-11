# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # recursive solution
        if(len(nums) == 0):
            return None
        if(len(nums) == 1):
            return TreeNode(nums[0])
        
        root_idx = (len(nums)-1)/2
        root = TreeNode(nums[root_idx])
        
        root.left = self.sortedArrayToBST(nums[0:root_idx])
        root.right = self.sortedArrayToBST(nums[root_idx+1:])
        return root