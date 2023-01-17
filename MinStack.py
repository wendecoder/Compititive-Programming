class MinStack:

    def __init__(self):
        self.stack1 = []

    def push(self, val: int) -> None:
        self.stack1.append(val)

    def pop(self) -> None:
        self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return min(self.stack1)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
