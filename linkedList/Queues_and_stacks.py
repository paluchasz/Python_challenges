'''In this program I want to implement a queue and a stack'''

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
            print("List is empty so cannot dequeue")

    def getLast(self):
        return self.queue[len(self.queue) - 1]

class Stack:
    def __init__(self, stack =[]):
        self.stack = stack

    def getStack(self):
        return self.stack

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():  #just another way of doing this, if already empty then
            return None     #return nothing
        else:
            self.stack.pop()

    def getLast(self):
        return self.stack[len(self.stack) - 1] 

if __name__ == '__main__':
    # new_queue = Queue([2,3])
    # print(new_queue.getQueue())
    # new_queue.enqueue(2)
    # print(new_queue.getQueue())
    # new_queue.dequeue()
    # print(new_queue.getQueue())
    # new_queue.dequeue()
    # print(new_queue.isEmpty())
    # new_queue.dequeue()
    # print(new_queue.isEmpty())
    # print(new_queue.getQueue())
    # new_queue.dequeue()

    new_stack = Stack()
    print(new_stack.isEmpty())
    new_stack.pop()
    print(new_stack.getStack())
    new_stack.push(4)
    print(new_stack.getStack())
