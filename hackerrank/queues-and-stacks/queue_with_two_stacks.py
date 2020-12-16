class MyQueue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []
    
    def __refill_outbox__(self):
        for i in range(len(self.inbox)):
                self.outbox.append(self.inbox.pop())

    def peek(self):
        if len(self.outbox) == 0:
            self.__refill_outbox__()
        return self.outbox[-1]        
        
        
    def pop(self):
        if len(self.outbox) == 0:
            self.__refill_outbox__()
        return self.outbox.pop()        
        
    def put(self, value):
        self.inbox.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
