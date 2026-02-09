'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        if not head or not head.next:
            return head
        zeroD = Node(0)
        oneD = Node(0)
        twoD = Node(0)
        zero = zeroD
        one = oneD
        two = twoD
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None 
        head = zeroD.next
        return head
    
