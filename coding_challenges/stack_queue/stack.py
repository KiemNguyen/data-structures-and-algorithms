class Stack:

    # Stack constructor
    def __init__(self, s):
        self.size = s
        self.stackArray = []
        self.top = -1

    # Check if stack is empty
    def is_empty(self):
        if self.top == -1:
            return True
        return False

    # Check if stack is full
    def is_full(self):
        if self.top == self.size - 1:
            return True
        return False

    # Return the top element
    def get_top(self):
        if not self.is_empty():
            return self.stackArray[self.top]
        else:
            print("Stack is empty")

    # Insert element at the top
    def push(self, value):
        if self.is_full() is True:
            return "Stack is full"
        self.top += 1
        self.stackArray.insert(self.top, value)

    # Remove and return element at the top
    def pop(self):
        if not self.is_empty():
            temp = self.stackArray[self.top]
            self.top -= 1
            return temp
        return "Stack is empty"


stack = Stack(5)

for i in range(5):
    stack.push(i)

print("Is stack full? {} ".format(stack.is_full()))
print("get Top: {} ".format(stack.get_top()))

for i in range(5):
    print(stack.pop())

print("Is stack empty? {} ".format(stack.is_empty()))