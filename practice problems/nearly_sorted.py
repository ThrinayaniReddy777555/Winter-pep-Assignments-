from heapq import heappush
from heapq import heappop

class Solution:

    def nearlySorted(self, arr, k):
        n = len(arr)
        heap = []
        index = 0
        for i in range(min(k+1, n)):
            heappush(heap, arr[i])
        for i in range(k+1, n):
            arr[index] = heappop(heap)
            index += 1
            heappush(heap, arr[i])
        while heap:
            arr[index] = heappop(heap)
            index += 1
        return arr