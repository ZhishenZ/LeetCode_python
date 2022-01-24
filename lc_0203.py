# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        cur_node = head
        pre_node = None

        while cur_node:

            if cur_node.val == val:

                # x-O-x
                if pre_node is None and cur_node.next is None:
                    return None

                # x-O-O
                elif pre_node is None:
                    head = cur_node.next
                    cur_node = cur_node.next
                    pre_node = None

                # O-O-x
                elif cur_node.next is None:
                    pre_node.next = None
                    return head

                # O-O-O
                else:
                    pre_node.next = cur_node.next
                    cur_node = cur_node.next

            else:
                pre_node = cur_node
                cur_node = cur_node.next




        return head


l1 = ListNode(val = 1)
l2 = ListNode(val = 2)
l3 = ListNode(val = 6)
l4 = ListNode(val = 3)
l5 = ListNode(val = 4)
l6 = ListNode(val = 5)
l7 = ListNode(val = 6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7




n1 = ListNode(val = 7)
n2 = ListNode(val = 7)
n3 = ListNode(val = 7)
n4 = ListNode(val = 7)
n1.next = n2
n2.next = n3
n3.next = n4




solution = Solution()
# l1_cleaned = solution.removeElements(l1, 6)
# while (l1_cleaned):
#     print(l1_cleaned.val)
#     l1_cleaned = l1_cleaned.next

n_cleaned = solution.removeElements(n1, 7)
while (n_cleaned):
    print(n_cleaned.val)
    n_cleaned = n_cleaned.next