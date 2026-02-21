'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

from collections import deque
class Solution:
    def depthOfOddLeaf(self,root):
        q=deque()
        q.append(root)
        level=0
        ans=0
        while len(q)>0:
            temp=[]
            level+=1
            while len(q)>0:
                curr = q.popleft()
                temp.append(curr)
                if curr.left == curr.right == None and level%2!=0:
                    ans = level
            for node in temp:
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        return ans
        #code here