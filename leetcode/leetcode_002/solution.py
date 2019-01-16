class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """       
        if(l1 is None and l2 is None):
            return None

        head = ListNode(0)
        point = head
        carry = 0
        while l1 is not None and l2 is not None:
            s = carry + l1.val + l2.val
            point.next = ListNode(s % 10)
            carry = s / 10
            l1 = l1.next
            l2 = l2.next
            point = point.next
            
        while l1 is not None:
            s = carry + l1.val
            point.next = ListNode(s % 10)
            carry = s / 10
            l1 = l1.next
            point = point.next
        
        while l2 is not None:
            s = carry + l2.val
            point.next = ListNode(s % 10)
            carry = s / 10
            l2 = l2.next
            point = point.next
    
        if carry != 0:
            point.next = ListNode(carry)

        return head.next