'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

from xml.dom import Node


class Solution:
    def insertAtPos(self, head, p, x):
        new_node=Node(x)
        if not head:
            head=new_node
            return head
        
        current=head
        count=0
        while current and count <p:
            current=current.next
            count=count+1
            
        if current is None:
            return head
        
        new_node.next=current.next
        new_node.prev=current
        if current.next is not None:
            current.next.prev=new_node
        current.next=new_node
    
        return head
        
        