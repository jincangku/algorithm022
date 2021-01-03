# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if (len(preorder) == 0) or (len(inorder) == 0):
            return None

        root_val = preorder[0]
        del preorder[0]
        index = inorder.index(root_val)
        left = self.buildTree(preorder, inorder[:index])
        right = self.buildTree(preorder, inorder[index + 1:])
        root = TreeNode(root_val, left, right)

        return root
