class Solution:
    def sumOfMax(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        total_sum = 0
        for i in range(n):
            total_sum += arr[i] * (i - left[i]) * (right[i] - i)
            
        return total_sum
