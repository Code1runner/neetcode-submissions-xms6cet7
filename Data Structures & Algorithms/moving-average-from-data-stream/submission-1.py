class MovingAverage:

    def __init__(self, size: int):
        self.window = []
        self.size = size
        self.l = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        if len(self.window) > self.size:
            self.l += 1
        return sum(self.window[self.l:]) / len(self.window[self.l:])


#[3,1,10] l=0 , r = 3
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
