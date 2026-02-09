# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: # type: ignore
        if not head or not head.next or k==0:
            return head 
        length = 1
        last_node = head
        while last_node.next:
            length+=1
            last_node=last_node.next
        last_node.next=head
        k%=length
        rotate_position = length-k
        new_tail = head
        for i in range(rotate_position-1):
            new_tail=new_tail.next
        new_head=new_tail.next 
        new_tail.next=None
        return new_head

        
