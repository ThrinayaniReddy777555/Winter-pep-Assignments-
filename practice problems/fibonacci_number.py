class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1
        
        # Iterate from 2 to n
        for _ in range(2, n + 1):
            a, b = b, a + b
            
        return b
     