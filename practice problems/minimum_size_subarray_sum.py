class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left = 0
        current_sum = 0
        ans = float("inf")
        for right in range(n):
            current_sum += nums[right] 
            print(current_sum)
            while current_sum >= target:
                ans = min(ans,right-left+1)
                current_sum -= nums[left]
                left += 1
        return 0 if ans == float('inf')else ans

