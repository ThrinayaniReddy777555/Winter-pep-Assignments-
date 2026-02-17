from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(capacity):
            d = 1
            load = 0
            for w in weights:
                if load + w > capacity:
                    d += 1
                    load = w
                    if d > days:
                        return False
                else:
                    load += w
            return True

        start, end = max(weights), sum(weights)
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            if check(mid):
                ans = mid
                end = mid - 1    
            else:
                start = mid + 1  

        return ans

