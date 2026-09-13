class MinStack:

    def __init__(self):
        self.stack = []
        self.MinS = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) > 1:
            val = min(val, self.getMin())
        self.MinS.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MinS.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinS[-1]
