
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n_1 = TreeNode(val = 1)
n_2 = TreeNode(val = 2)
n_3 = TreeNode(val = 3)

n_1.right = n_2
n_2.left = n_3

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        my_list = []
        def helper(node):
            if node is None:
                return 
            helper(node.left)
            my_list.append(node.val)
            helper(node.right)
            return 
        helper(root)
        return my_list

solution = Solution()
print(solution.preorderTraversal(n_1))