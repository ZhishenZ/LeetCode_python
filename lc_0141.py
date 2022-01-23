



from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head, head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
            
            
        return False


class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()
        
        if head is None:
            return False
        
        while head:
            if head.next is None:
                return False
            
            if head.next in my_set:
                return True
            my_set.add(head)
            head = head.next
        return False