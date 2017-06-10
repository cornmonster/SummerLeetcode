class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # The idea is to split the numbers in to tow sub trees
        # For example, if n=3, we will take one num as root,
        # and the # of nodes in two subtrees will be 2:0, 1:1,
        # or 0:2.
        num_trees = [1, 1]
        for i in xrange(2, n+1):
            temp_sum = 0
            for j in xrange(0, i):
                temp_sum += num_trees[j] * num_trees[i-j-1]
            num_trees.append(temp_sum)
        
        print num_trees
        return num_trees[n]

s = Solution()
print s.numTrees(3)