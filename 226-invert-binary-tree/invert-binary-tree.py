# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def switch_tree(root):
            if root:
                left = root.left
                right = root.right
                root.left = right
                root.right = left
                switch_tree(left)
                switch_tree(right)

        switch_tree(root)

        return root