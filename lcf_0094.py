from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        
        
        def recursion(node: Optional[TreeNode]):
            if node is None:
                return 
            
            recursion(node.left)
            output.append(node.val)
            recursion(node.right)
            return
        
        recursion(root)
        
        return output