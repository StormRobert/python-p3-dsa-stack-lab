class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        pass

    def full(self):
        pass

    def search(self, target):
        pass
