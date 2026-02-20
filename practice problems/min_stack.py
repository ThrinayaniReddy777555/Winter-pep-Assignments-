class MinStack:
    def __init__(self):
        # Main stack to store all elements
        self.stack = []
        # Auxiliary stack to store minimums
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to minStack: either the new val or the current min
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
