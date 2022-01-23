from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        
        def helper(root,cur_sum):
            
            cur_sum += root.val

            if root.left is None and root.right is None:
                if cur_sum == targetSum:
                    return True
                else:
                    return False
            
            if root.left is None:
                return helper(root.right,cur_sum)

            if root.right is None:
                return helper(root.left,cur_sum)

            return helper(root.left,cur_sum) or helper(root.right,cur_sum)
            

        cur_sum = 0

        return helper(root,cur_sum)