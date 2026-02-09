#python code 
 
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
'''
from xml.dom import Node


class Solution:
    def constructDLL(self, arr): 
        if not arr:
            return None
        
        head=Node(arr[0])
        cur=head
        
        for i in range(1,len(arr)):
            new_node=Node(arr[i])
            cur.next=new_node
            new_node.prev=cur
            cur=new_node
        return head