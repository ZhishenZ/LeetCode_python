
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        hA = headA
        hB = headB
        
        while headA!=headB:
            
            headA = hB if headA is None else headA.next
            headB = hA if headB is None else headB.next
        
        return headA

# class Solution2:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
#         hA = headA
#         hB = headB
        
#         while headA or headB:
#             if headA==headB:
#                 return headA
#             headA = hB if headA is None else headA.next
#             headB = hA if headB is None else headB.next 





# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
#         set_a = set()
#         set_b = set()
        
#         while headA or headB:
            
#             if headA:
#                 if headA in set_b:
#                     return headA
#                 set_a.add(headA)
#                 headA = headA.next
            
#             if headB:
#                 if headB in set_a:
#                     return headB
#                 set_b.add(headB)
#                 headB = headB.next
                
#         return None
