# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def search_branch(root):
            if root:
                left, right = root.left, root.right

                max_left = search_branch(left)

                max_right = search_branch(right)

                return max(max_left, max_right) + 1 
            else:
                return 0

        return search_branch(root)




