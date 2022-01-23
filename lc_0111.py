


from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def helper(root):


            if root is None:
                return inf
            
            if root.left is None and root.right is None:
                return 1

            return  (1 + min(helper(root.left), helper(root.right)))



        return helper(root)