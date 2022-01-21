from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree_head_1 = TreeNode(val = 1, left = None, right = TreeNode(val = 2))
tree_head_2 = TreeNode(val = 1, left = TreeNode(val = 2), right = None )


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        elif p.val!=q.val:
            return False
        
        return (self.isSameTree( p.left, q.left) and self.isSameTree( p.right, q.right))


solution = Solution()
return_value = solution.isSameTree(tree_head_1,tree_head_2)
print(return_value)
        