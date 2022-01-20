# coding=UTF-8
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.







# 找一下什么是optional
from tkinter.tix import ListNoteBook
from typing import Optional
from unittest import result
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l13 = ListNode(3,None)
l12 = ListNode(4,l13)
l11 = ListNode(2,l12)

l23 = ListNode(4,None)
l22 = ListNode(6,l23)
l21 = ListNode(5,l22)

l1 = [l11,l12,l13]
l2 = [l21,l22,l23]

l37 = ListNode(9,None)
l36 = ListNode(9,l37)
l35 = ListNode(9,l36)
l34 = ListNode(9,l35)
l33 = ListNode(9,l34)
l32 = ListNode(9,l33)
l31 = ListNode(9,l32)

l44 = ListNode(9,None)
l43 = ListNode(9,l44)
l42 = ListNode(9,l43)
l41 = ListNode(9,l42)

l3 = [l31,l32,l33,l34,l35,l36,l37]
l4 = [l41,l42,l43,l44]


l0 =  ListNode(0,None)

# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        this_node = ListNode()
        head_node = this_node
        add_1 = 0
        print("Because python is not using deep copy for mutable variables!")
        print("and we have: ")
        print("the id(address) of this_node is {}".format(id(this_node)))
        print("the id(address) of head_node is {}".format(id(head_node)))

        print("the id(address) of this_node.next is {}".format(id(this_node.next)))
        print("the id(address) of head_node.next is {}".format(id(head_node.next)))

        while((l1 is not None) or (l2 is not None) or (add_1 ==1)):

            if(l1 is None):
                val_1 = 0
            else:
                val_1 = l1.val
                l1 = l1.next

            if(l2 is None):
                val_2 = 0
            else:
                val_2 = l2.val
                l2 = l2.next


            if ((val_1 + val_2 + add_1)>=10):
                val = (val_1 + val_2 + add_1)-10
                add_1 = 1
            else:
                val = val_1 + val_2 + add_1
                add_1 = 0

            this_node.next = ListNode(val =val)
            this_node = this_node.next

        this_node.next = None

        return head_node.next

solution = Solution 
return_nvalue = solution.addTwoNumbers(solution,l0,l0)
while(return_nvalue.next is not None):
    print(return_nvalue.val)
    return_nvalue = return_nvalue.next
print(return_nvalue.val)

        # # we assume that the l1 is the longest
        # chosen_list = l1 # choose the long list
        # large_length = len(l1)
        # small_length = len(l2)
        # if(large_length< len(l2)):
        #     small_length = large_length
        #     large_length = len(l2)
        #     chosen_list = l2
        # add1 = False
        # added_number = 0


        # # add the shared digits
        # for i in range(small_length):
        #     if(add1 == True):
        #         added_number = 1
        #     else:
        #         added_number = 0

        #     if ((l1[i].val + l2[i].val + added_number)>=10):
        #         chosen_list[i].val = (l1[i].val + l2[i].val + added_number)%10
        #         add1 = True
        #     else: 
        #         chosen_list[i].val = (l1[i].val + l2[i].val + added_number)
        #         add1 = False
        # # add the bigger number
        # if((small_length!=large_length)and(add1 == True)):
        #     for i in range(small_length,large_length):
        #         if ((chosen_list[i].val+1)>=10):
        #             chosen_list[i].val = (chosen_list[i].val+1)%10
        #         else:
        #             chosen_list[i].val += (chosen_list[i].val+1)%10
        #             break
        
        # # if the last number is 0
        # if(chosen_list[large_length-1].val == 0):
        #     print("test")
        #     chosen_list[large_length-1].next = ListNode(1,None)
        #     chosen_list.append(chosen_list[large_length-1].next)


        # return chosen_list





