from xml.dom import Node


class Solution:
    def sortedInsert(self, head, key):
        # code here
        # return head of edited linked list
        temp = head
        new = Node(key)
        if temp.data>=key:
            new.next=temp
            return new
        while temp.next is not None:
            if temp.next.data>key:
                new.next = temp.next
                temp.next = new
                return head
            temp=temp.next
        temp.next=new
        return head
            
            
        