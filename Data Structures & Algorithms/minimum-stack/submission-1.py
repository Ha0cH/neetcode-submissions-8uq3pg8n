class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minNum:
            self.minNum.append(val)
        else:
            self.minNum.append(min(val, self.minNum[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minNum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minNum[-1]
