# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
    
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = x + y + carry
        
            # Update carry for next calculation
            carry = sum / 10
            # Create a new node with the digit value of sum mod 10 
            # and set it to current node's next, then advance current node to next.
            curr.next = ListNode(sum % 10)
            curr = curr.next
        
            # Advance both p and q
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        # Check if carry = 1, if so append 1 to a new node to return list
        if (carry > 0):
            curr.next = ListNode(carry)
        return dummyHead.next
    
