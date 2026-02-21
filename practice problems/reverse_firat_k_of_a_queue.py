
class Solution:
    def reverseFirstK(self, q, k):
        st=[]
        n=len(q)
        if k > n or k <= 0:
            return q
        
        for _ in range(k):
            st.append(q.popleft())
        
        while st:
            q.append(st.pop())
            
        for _ in range(len(q)-k):
            q.append(q.popleft())
        
        return q