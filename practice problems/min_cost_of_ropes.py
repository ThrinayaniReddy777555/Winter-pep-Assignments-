import heapq

class Solution:
    def minCost(self, arr):
        # If only one or no rope, cost is 0
        if len(arr) <= 1:
            return 0

        # Convert list into min heap
        heapq.heapify(arr)

        total_cost = 0

        # Keep joining until one rope is left
        while len(arr) > 1:
            first = heapq.heappop(arr)   # smallest rope
            second = heapq.heappop(arr)  # second smallest rope

            new_rope = first + second
            total_cost += new_rope

            heapq.heappush(arr, new_rope)

        return total_cost

