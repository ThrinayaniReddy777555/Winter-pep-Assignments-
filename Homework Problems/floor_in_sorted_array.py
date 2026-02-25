
class Solution:
    def findFloor(self, arr, x):
        index = -1
        
        for i in range(0, len(arr)):
            if arr[i] <= x:
                index = i
            
        return index