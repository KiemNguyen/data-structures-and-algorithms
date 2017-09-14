# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorder(self, root):
        if root is None:
            return
            
        self.inorder(root.left)
        self.output.append(root.val)
        self.inorder(root.right)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.output = []
        self.inorder(root)
        return self.output == sorted(self.output) and len(set(self.output)) == len(self.output)

root = TreeNode(0)
root.val = 2
root.left = TreeNode(0)
root.left.val = 1
root.right = TreeNode(0)
root.right.val = 3

solution = Solution()
solution.validate(root)
