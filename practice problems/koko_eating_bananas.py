from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right       
        while left <= right:
            k = (left + right) // 2
            total_time = 0           
            for p in piles:
                total_time += (p + k - 1) // k   
                if total_time > h:
                    break            
            if total_time <= h:
                res = k
                right = k - 1
            else:
                left = k + 1                
        return res