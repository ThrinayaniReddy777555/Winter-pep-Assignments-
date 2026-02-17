
class Solution:
    def reverseingroups(self, arr, k):
        n=len(arr)
        if n<=k:
            arr.reverse()
            return 
        for i in range(0,n,k):
            arr[i:i+k] = (arr[i:i+k])[::-1]
            