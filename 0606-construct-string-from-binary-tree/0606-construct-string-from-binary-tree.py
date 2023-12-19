# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root: #base case
            return ''
        
        string = str(root.val)
        if root.left:
            string += '(' + self.tree2str(root.left) + ')'
        if root.right:
            string += '()' if not root.left else ''
            string += '(' + self.tree2str(root.right) + ')'
        '''
        1 + (2 ()(4)) + (3)
        root + left + right
        '''
        return string