class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = [] #the last value should always be the min.

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minNum:
            self.minNum.append(val)
        else:
            if val <= self.minNum[-1]:
                self.minNum.append(val)
            else: #val > self.minNum[-1]
                self.minNum.append(val)
                self.minNum[-1], self.minNum[-2] = self.minNum[-2], self.minNum[-1]

    def pop(self) -> None:
        if self.stack[-1] == self.minNum[-1]:
            del self.minNum[-1]
        else:
            self.minNum[-1], self.minNum[-2] = self.minNum[-2], self.minNum[-1]
            del self.minNum[-1]
        
        del self.stack[-1]

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minNum[-1]
        
