class Solution:
    
    def heapify(self, arr, _len, i):
        
        largest = i
        left = 2 * largest + 1
        right = 2 * largest + 2
        
        if left < _len and arr[largest] < arr[left]:
            largest = left
        if right < _len and arr[largest] < arr[right]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, _len, largest)    
    
    def heapSort(self, arr):
        for index in range(len(arr)//2 - 1, -1, -1):
            self.heapify(arr,len(arr), index)
        for index in range(len(arr) - 1, 0, -1):
            arr[0], arr[index] = arr[index], arr[0]
            self.heapify(arr,index, 0) 