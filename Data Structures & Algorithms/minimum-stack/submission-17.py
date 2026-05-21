class MinStack:

    def __init__(self):
        self.minstack = []
        self.min_el = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        val = min(val, self.min_el[-1] if self.min_el else val)
        self.min_el.append(val)

 
    def pop(self) -> None:
        self.minstack.pop()
        self.min_el.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.min_el[-1]
