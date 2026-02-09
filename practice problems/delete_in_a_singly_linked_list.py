'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        curr=head
        if x==1:
            return head.next
        for i in range(x-2):
            curr = curr.next
        curr.next=curr.next.next
        return head

