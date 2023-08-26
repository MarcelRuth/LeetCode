# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return true
        return self.check_tree(root.left, root.right)
        
    def check_tree(self, left_root, right_root):

        # treat it like checking for if equal but invert left and right
        if left_root == None and right_root == None:

            # both are none, hence the end is reached with no
            # error -> has to be symmetric
            return True

        if left_root == None or right_root == None:
            # one of both sides None
            # return False
            return False

        if left_root.val == right_root.val:
            return self.check_tree(left_root.left, right_root.right) and self.check_tree(left_root.right, right_root.left)
        else:
            return False
