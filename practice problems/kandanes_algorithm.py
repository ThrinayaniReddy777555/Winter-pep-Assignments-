class Solution:
    def maxSubarraySum(self, arr):
        # res = arr[0]
        # for i in range(len(arr)):
        #     curr_sum =0
        #     for j in range(i,len(arr)):
        #         curr_sum += arr[j]
        #         res = max(res,curr_sum)
        # return res
        # Code here
        if not arr:
            return 0
        max_sum = arr[0]
        curr_sum = arr[0]
        for i in range(1,len(arr)):
            curr_sum = max(arr[i],curr_sum+arr[i])
            max_sum = max(max_sum,curr_sum)
        return max_sum
            
            
       