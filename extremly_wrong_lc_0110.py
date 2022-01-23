
from doctest import BLANKLINE_MARKER
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


n_1 = TreeNode(val = 1)
n_2 = TreeNode(val = 2)
n_3 = TreeNode(val = 3)
n_4 = TreeNode(val = 4)
n_5 = TreeNode(val = 5)
n_6 = TreeNode(val = 6)
n_7 = TreeNode(val = 7)
n_1.left = n_2
n_1.right = n_3
n_2.left = n_4
n_2.right = n_5
n_4.left = n_6
n_4.right = n_7

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def helper (root):
  
            if root is None:
                return True, 0
            if root.left is None and root.right is None:
                return True, 1


            left_called = helper(root.left)
            right_called = helper(root.right)
            balanced = left_called[0] and right_called[0] and (abs(right_called[1] - left_called[1])<2)
            depth = max(right_called[1], left_called[1])+1


            return balanced, depth
        
        return helper(root)[0]


solution = Solution()

print(solution.isBalanced(n_1))