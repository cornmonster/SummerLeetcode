# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, nums):
        ''' helper returns all the possible BSTs made up by nums
        '''
        if(len(nums) == 0):
            return []
        if(len(nums) == 1):
            return [TreeNode(nums[0])]
        if(len(nums) == 2):
            root_1 = TreeNode(nums[0])
            root_1.right = TreeNode(nums[1])
            root_2 = TreeNode(nums[1])
            root_2.left = TreeNode(nums[0])
            return [root_1, root_2]
        
        res = []
        for i in xrange(len(nums)):
            if(i == 0):
                for right_subtree in self.helper(nums[i+1:]):
                    root = TreeNode(nums[i])
                    root.right = right_subtree
                    res.append(root)
            elif(i == len(nums)-1):
                for left_subtree in self.helper(nums[0:i]):
                    root = TreeNode(nums[i])
                    root.left = left_subtree
                    res.append(root)
            else:
                for left_subtree in self.helper(nums[0:i]):
                    for right_subtree in self.helper(nums[i+1:]):
                        root = TreeNode(nums[i])
                        root.left = left_subtree
                        root.right = right_subtree
                        res.append(root)
        
        return res
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if(n == 0):
            return []

        nums = []
        for i in xrange(n):
            nums.append(i+1)

        return self.helper(nums)