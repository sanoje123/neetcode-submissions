class MinStack:

    def __init__(self):
        self.stack = []
        self.minEl = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.minEl.append(val)
        self.stack.append(val)

        if val < self.minEl[-1]:
            self.minEl.append(val)
        else:
            self.minEl.append(self.minEl[-1])

    def pop(self) -> None:
        self.minEl.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minEl[-1]
        
