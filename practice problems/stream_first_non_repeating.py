from collections import deque
class Solution:
    def firstNonRepeating(self, s):
# code here
        res, d, q, n = "", {}, deque(), len(s)
        for i in range(n):
            d[s[i]] = d.get(s[i], 0) + 1
            q.append(s[i])
            while(q and d[q[0]] > 1):
                q.popleft()
            if q:
                res += q[0]
            else:
                res += '#'
        return res