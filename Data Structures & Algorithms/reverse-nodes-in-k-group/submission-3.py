# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        while True:
            kth = self.getkth(dummy, k)
            if not kth:
                return res.next
            
            groupNext = kth.next
            cur, prev = dummy.next, kth.next

            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = dummy.next
            dummy.next = kth
            dummy = temp
        
        return res.next

    
    def getkth(self, head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head
