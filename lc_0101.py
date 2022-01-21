from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree_head_1 = TreeNode(val = 1, left = None, right = TreeNode(val = 2))
tree_head_2 = TreeNode(val = 1, left = TreeNode(val = 2), right = None )


class Solution(object):


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        elif p.val!=q.val:
            return False
        
        return (self.isSameTree( p.left, q.left) and self.isSameTree( p.right, q.right))

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        p = root.left
        q = root.right

        return self.isSameTree(p, q)


solution = Solution()
return_value = solution.isSameTree(tree_head_1,tree_head_2)
print(return_value)
        