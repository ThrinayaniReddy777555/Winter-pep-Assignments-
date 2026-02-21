
class Solution:
    def nextSmallerEle(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                res[index] = arr[i]
            stack.append(i)
            
        return res

		# code here