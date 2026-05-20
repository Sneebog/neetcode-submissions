class MinStack:

    def __init__(self):
        self.minstack = []
        self.tail = -1
        self.min_val = None   # FIX: use None instead of ""

    def push(self, val: int) -> None:
        if self.min_val is None or self.min_val > val:
            self.min_val = val
        self.minstack.append(val)
        self.tail += 1

    def pop(self) -> None:
        if self.tail != -1:
            check_val = self.minstack.pop()
            self.tail -= 1

            if self.tail == -1:
                # FIX: reset when stack becomes empty
                self.min_val = None
            elif check_val == self.min_val:
                self.min_val = min(self.minstack)

    def top(self) -> int:
        if self.tail != -1:
            return self.minstack[-1]

    def getMin(self) -> int:
        return self.min_val
        if check_val == self.min_val and self.tail != -1:
            self.min_val = min(self.minstack)

    def top(self) -> int:
        if self.tail != -1:
            return self.minstack[-1]

    def getMin(self) -> int:
        return self.min_val

