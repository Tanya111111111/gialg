#143. Reorder List
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        p = None
        while slow:
            n = slow.next
            slow.next = p
            p = slow
            slow = n
        
        x = head
        y = p
        while y.next:
            t1 = x.next
            t2 = y.next
            x.next = y
            y.next = t1
            x = t1
            y = t2