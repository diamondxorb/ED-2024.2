class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
