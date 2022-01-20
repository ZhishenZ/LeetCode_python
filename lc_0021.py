from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:



        head_node = ListNode()
        this_node = head_node

        while list1 or list2:
            
            val_1 = 100 if list1 is None else list1.val
            val_2 = 100 if list2 is None else list2.val
                
            if val_1 < val_2:
                this_node.next = ListNode(val = val_1)              
                if list1 is not None:
                    list1 = list1.next

            else:
                this_node.next = ListNode(val = val_2)
                if list2 is not None:
                    list2 = list2.next
                    
            this_node = this_node.next
            
            
            this_node.next = None

        return head_node.next





# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]