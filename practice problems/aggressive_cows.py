class Solution:
    def canPlaceCowsatMidDist(self,arr,mid,c):
        cowCount=1
        prevCowPos=arr[0]
        for i in range(1,len(arr)):
            if arr[i]-prevCowPos>=mid:
                cowCount+=1
                prevCowPos=arr[i]
        if cowCount<c:
            return False
        return True
    def solve(self,arr,n,c):
        s=0
        e=arr[-1]-arr[0]
        ans=-1
        while s<=e:
            mid=s+(e-s)//2
            if self.canPlaceCowsatMidDist(arr,mid,c):
                ans=mid
                s=mid+1
            else:
                e=mid-1
        return ans

    def aggressiveCows(self,stalls,k):
        stalls.sort()
        return self.solve(stalls,len(stalls),k)