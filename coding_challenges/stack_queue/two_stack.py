class TwoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = []
        self.top1 = -1
        self.top2 = self.size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr.insert(self.top1, value)

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr.insert(self.top2, value)

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 >= 0:
            temp = self.arr[self.top1]
            self.top1 -= 1
            return temp
        return -1

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top2 < self.size:
            temp = self.arr[self.top2]
            self.top2 += 1
            return temp
        return -1
