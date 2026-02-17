class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        cur_max = cur_min = 0
        max_sum = nums[0]
        min_sum = nums[0]
        total_sum = 0
        
        for n in nums:
            cur_max = max(cur_max + n, n)
            max_sum = max(max_sum, cur_max)
            
            cur_min = min(cur_min + n, n)
            min_sum = min(min_sum, cur_min)
            
            total_sum += n
        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        return max_sum
     
        