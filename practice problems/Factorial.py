from math import factorial


class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        if n==1 or n==0:
            return 1
        return self.factorial(n) * factorial(n-1)
    