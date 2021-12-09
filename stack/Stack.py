
class Stack:

    def __init__(self):
        self.elements = []
    
    def peek(self):
        return self.elements[-1]
    
    def push(self,data):
        self.elements.append(data)
        return data

    def pop(self):
        return self.elements.pop()

    def isEmpty(self):
        return len(self.elements) == 0
    
    def print_stack(self):
        print(self.elements)

    def size(self):
        return len(self.elements)


    