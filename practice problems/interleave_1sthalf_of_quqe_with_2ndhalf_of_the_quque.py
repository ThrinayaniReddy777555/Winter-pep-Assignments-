from collections import deque


class Solution:
    def rearrangeQueue(self, q):
        r=deque()
        half = len(q)//2
        for i in range(half):
            r.append(q.popleft())
        for j in range(half):
            q.append(r.popleft())
            q.append(q.popleft())
        #code here 