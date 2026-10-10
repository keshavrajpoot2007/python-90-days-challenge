# Problem Statement

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            
            if l1:
                val1 = l1.val
                l1 = l1.next      
            else:
                val1 = 0

         
            if l2:
                val2 = l2.val
                l2 = l2.next      
            else:
                val2 = 0

            total = val1 + val2 + carry

            current.next = ListNode(total % 10)
            current = current.next
            carry = total // 10

        return dummy.next
            

        
        