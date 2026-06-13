#143. Reorder List
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        a = b = head
        while b and b.next:
            a = a.next
            b = b.next.next
        
        p = None
        while a:
            n = a.next
            a.next = p
            p = a
            a = n
        
        x = head
        y = p
        while y.next:
            t1 = x.next
            t2 = y.next
            x.next = y
            y.next = t1
            x = t1
            y = t2