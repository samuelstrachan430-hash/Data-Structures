class queue:
    def __init__(self, head = 0, tail = 0): #tail points to the next empty slot, head points to the first element in the queue
        self.items = [None] * 10
        self.head = head
        self.tail = tail
        self.size = 0

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.size() < 10:
            self.items[self.tail] = item
            self.tail += 1
            self.size +=1

    def dequeue(self):
        if self.isEmpty():
            raise Exception ("queue is empty")
        else:
            item = self.items[self.head] 
            self.head += 1
            self.size -= 1
            return item
    
    def Getsize(self):
        return self.size
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[self.head]

    def isFull(self):
        if self.size == 10:
            return True
        else:
            return False 

class stack:
    def __init__(self):
        self.items = [None] * 10
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, item):
        if self.size() < 9:
            self.top += 1
            self.items[self.top] = item
        else:
            raise Exception ("stack is full")

    def pop(self):
        if self.isEmpty() == True:
            raise Exception ("stack is empty")
        else:
            item = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return item

    def size(self):
        return self.top + 1
    
    def peek(self):
        if self.isEmpty() == True:
            raise Exception ("stack is empty")
        else:
            return self.items[self.top]

    def isFull(self):
        if self.size() == 9:
            return True
        else:
            return False
        
class circularQueue:
    def __init__(self, head = 0, tail = 0):
        self.items = [None] * 10
        self.head = head
        self.tail = tail
        self.count = 0 

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.count < 10:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % 10
            self.count += 1
        else:
            raise Exception ("queue is full")

    def dequeue(self):
            if not self.isEmpty():
                item = self.items[self.head]
                self.items[self.head] = None
                self.count -= 1
                self.head = (self.head + 1) % 10
                return item
            else:
                raise Exception("queue is empty")

    def size(self):
        return self.count
    
    def peek(self):
        if self.isEmpty():
            raise Exception ("queue is empty")
        else:
            return self.items[self.head]

    def isFull(self):
        if self.size() == 10:
            return True
        else:
            return False
        
