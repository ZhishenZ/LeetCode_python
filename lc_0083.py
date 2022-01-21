
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        node = self
        while (node):
            print(node.val)
            node = node.next




class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = ListNode(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = ListNode(value)
        return

    def print_linked_list(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.val)
            current_node = current_node.next

ld_1 = LinkedList()
ld_1.append(1)
ld_1.append(1)
ld_1.append(2)
ld_1.append(1)
ld_1.append(1)
ld_1.append(2)
head_1 = ld_1.head

ld_2 = LinkedList()
ld_2.append(1)
ld_2.append(1)
ld_2.append(2)
ld_2.append(3)
ld_2.append(1)
ld_2.append(2)
ld_2.append(2)
head_2 = ld_2.head

ld_3 = LinkedList()
ld_3.append(1)
ld_3.append(1)
ld_3.append(2)
ld_3.append(3)
ld_3.append(2)
ld_3.append(2)
ld_3.append(2)
head_3 = ld_3.head

ld_4 = LinkedList()
head_4 = ld_4.head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        if not head.next:
            return head
        
        cur_node = head
        while cur_node.next.next:
            if cur_node.next.val == cur_node.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        # the last two elements
        if cur_node.next.val == cur_node.val:
                cur_node.next = None 
        return head





class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if not head:
            return None

        cur_node = head
        while cur_node.next:
            if cur_node.next.val == cur_node.val:
                if cur_node.next.next:
                    cur_node.next = cur_node.next.next
                else: 
                    cur_node.next = None
                    return head
            else:
                cur_node = cur_node.next
        cur_node.next = None   
        return head


soultion2 = Solution2()

node2 = soultion2.deleteDuplicates(head_3)
if node2: node2.print()
# while (node):
#     print(node.val)
#     node = node.next

