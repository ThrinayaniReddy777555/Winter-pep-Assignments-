# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:#type: ignore 
        def reverse(start, end):
            prev = end
            while start != end:
                temp = start.next
                start.next = prev
                prev = start
                start = temp
            return prev
        
        dummy = ListNode(0) # type: ignore
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next
            start = group_prev.next
            group_prev.next = reverse(start, group_next)
            group_prev = start        
        