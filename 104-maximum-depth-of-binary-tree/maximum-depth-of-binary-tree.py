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


# BFS Approach

# def maxDepth(self, root: TreeNode) -> int:
    
#     if not root: return 0
    
#     queue = [(root, 1)]
#     self.res = 0
    
#     while queue:
#         root, nums = queue.pop(0)
        
#         if not root.left and not root.right:
#             self.res = max(self.res, nums)
            
#         if root.left:
#             queue.append((root.left, nums + 1))
            
#         if root.right:
#             queue.append((root.right, nums + 1))
            
#     return self.res