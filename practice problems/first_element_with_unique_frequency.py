from collections import Counter
from typing import List

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        
        count_of_freqs = Counter(freq_map.values())
        for num in nums:

            if count_of_freqs[freq_map[num]] == 1:
                return num
                
        return -1

        