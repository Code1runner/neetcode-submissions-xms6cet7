class MinStack:

    def __init__(self):
        self.stack = []
        self.min_state = []
        self.curr_min = None

    def push(self, val: int) -> None:
        
        if len(self.stack) == 0:
            self.curr_min = val
        
        if val < self.curr_min:
            self.curr_min = val

        self.stack.append(val)
        self.min_state.append(self.curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_state.pop()
        self.curr_min = self.min_state[-1] if self.min_state else None
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_state[-1]        
