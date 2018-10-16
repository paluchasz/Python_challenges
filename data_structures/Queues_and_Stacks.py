class Queue:
    def __init__(self, queue = []):
        self.queue = queue

    def getQueue(self):
        return self.queue

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        try:
            self.queue.pop()
        except IndexError as error:
            print("Queue is empty so cannot dequeue")

    def getLast(self):
        return self.queue[len(self.queue) - 1]

class Stack:
    def __init__(self, stack = []):
        self.stack = stack

    def getStack(self):
        return self.stack

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        try:
            self.stack.pop()
        except IndexError as error:
            print("Stack is empty so cannot pop")

    def getLast(self):
        return self.stack[len(self.stack) - 1]
