"""
Push pairs to the stack (value, stack_min)

"""
class MinStack:

    def __init__(self):
        self.stack = [] # pairs (val, stack_min)

    def push(self, val: int) -> None:
        """
            if stack is empty:
                push (val, val)
            if stack is not empty:
                push (val, min(val, stack.top()[1]))
        """
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            new_stack_min = min(val, self.getMin())
            self.stack.append((val, new_stack_min))

    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()