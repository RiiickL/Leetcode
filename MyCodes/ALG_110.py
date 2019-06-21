# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def DegreeBalanceReturn(tree):
            if tree is None:
                return (True, 0)
            elif (tree.left==None) and (tree.right==None):
                return (True, 1)
            
            res_left = DegreeBalanceReturn(tree.left)
            res_right = DegreeBalanceReturn(tree.right)
            if (not res_left[0]) or (not res_right[0]):
                return (False, 0)
            if abs(res_left[1]-res_right[1])>1:
                return (False, 0)
            
            return (True, max(res_left[1], res_right[1])+1)
            
        res = DegreeBalanceReturn(root)
        return res[0]

        