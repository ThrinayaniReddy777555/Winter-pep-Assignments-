class Solution:
    def nthRoot(self, n, m):
       # code here
        l=0
        h=m
        while l<=h:
            mid=l+(h-l)//2
            if mid**n==m:
               return mid
            elif mid**n>m:
                h=mid-1
            else:
                l=mid+1
        return -1