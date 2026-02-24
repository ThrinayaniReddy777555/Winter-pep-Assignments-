import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        while max_heap:
            count, char = heapq.heappop(max_heap)
            count = -count 
            
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not max_heap:
                    break                 
                count_next, char_next = heapq.heappop(max_heap)
                count_next = -count_next
                
                res.append(char_next)
                count_next -= 1
                
                if count_next > 0:
                    heapq.heappush(max_heap, (-count_next, char_next))
                
                heapq.heappush(max_heap, (-count, char))
            else:
                res.append(char)
                count -= 1
                
                if count > 0:
                    heapq.heappush(max_heap, (-count, char))
                    
        return "".join(res)

