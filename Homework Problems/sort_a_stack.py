class Solution:
    # def sortStack(self, st):
    def insert(self, st, k):
        if not st or st[-1] <= k:
            st.append(k)
            return
        
        last = st.pop()
        self.insert(st, k)
        st.append(last)
        
    def sortStack(self, st):
        # code here 
        if len(st) <= 1:
            return st
        
        last = st.pop()
        self.sortStack(st)
        self.insert(st, last)
        return st    
    #     # code here 
