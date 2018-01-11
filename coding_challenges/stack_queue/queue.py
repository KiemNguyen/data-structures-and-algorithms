class Queue():

    def __init__(self, s):
        self.size = s
        self.queueArray = []
        self.front = 0
        self.back = -1
        self.num_of_items = 0

    # Check if queue is empty
    def is_empty(self):
        if self.num_of_items == 0:
            return True
        return False

    # Check if queue is full
    def is_full(self):
        if self.num_of_items == self.size:
            return True
        return False

    # Return the top element
    def get_top(self):
        if not self.is_empty():
            return self.queueArray[self.front]
        else:
            print("Queue is empty")

    # Return the size of queue
    def get_size(self):
        return self.num_of_items

    # Add item to queue
    def enqueue(self, value):
        if self.is_full() is True:
            print("Queue is full")
            return
        if self.back == self.size - 1:
            self.back = -1
        self.back += 1
        self.queueArray.insert(self.back, value)
        self.num_of_items += 1

    # Remove item from queue
    def dequeue(self):
        if self.is_empty() is True:
            print("Queue is empty")
            return
        temp = self.queueArray[self.front]
        self.front += 1
        if self.front == self.size:
            front = 0
        self.num_of_items -= 1
        return temp


queue = Queue(5)

queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(8)
queue.enqueue(10)

print("Is queue full? {}".format(queue.is_full()))

print("Dequeue {}".format(queue.dequeue()))
print("Dequeue {}".format(queue.dequeue()))
print("Dequeue {}".format(queue.dequeue()))

print(queue.get_top())

