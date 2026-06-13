#2. Add Two Numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is None:
                x = 0
            else:
                x = l1.val
                
            if l2 is None:
                y = 0
            else:
                y = l2.val
                
            summa = x + y + carry
            carry = summa // 10
            digit = summa % 10
            
            cur.next = ListNode(digit)
            cur = cur.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return dummy.next