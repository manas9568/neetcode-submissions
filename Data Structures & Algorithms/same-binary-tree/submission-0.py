# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def f(p,q):
            if not p or not q:
                return p==q
            if p.val != q.val:
                return False
            if not p and not q:
                return True
            return f(p.left,q.left) and f(p.right,q.right)
        return f(p,q)
        