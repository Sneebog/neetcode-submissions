class MinStack:

    def __init__(self):
        self.minstack = []
        self.min_el = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        if self.min_el and val > self.min_el[-1]:
            self.min_el.append(self.min_el[-1])
        else:
            self.min_el.append(val)
 
    def pop(self) -> None:
        self.minstack.pop()
        self.min_el.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.min_el[-1]
