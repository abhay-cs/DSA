
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

'''
testing part
'''
import unittest

class StackTester(unittest.TestCase):

    def test_stack_init(self):
        s = Stack()
        self.assertEqual(0, s.size())

    def test_push1_size(self):
        item = 5
        s = Stack()
        s.push(item)
        self.assertEqual(1, s.size())

    def test_push1_items(self):
        s = Stack()
        s.push(5)
        self.assertEqual([5], s.elements)

    def test_push2_size(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual(2, s.size())

    def test_push2_items(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual([5,6], s.elements)

    def test_push2_pop1_size(self):
        s = Stack()
        s.push(5)
        s.push(6)
        s.pop()
        self.assertEqual(1, s.size())

    def test_push2_pop1_value(self):
        s = Stack()
        s.push(8)
        s.push(9)
        self.assertEqual(9, s.pop())

    def test_push2_pop2_size(self):
        s = Stack()
        s.push("Glob")
        s.push("Blob")
        s.pop()
        s.pop()
        self.assertEqual(0, s.size())

    def test_push2_pop2_value(self):
        s = Stack()
        s.push("Glob")
        s.push("Blob")
        s.pop()
        self.assertEqual("Glob", s.pop())

    def test_isEmpty_init(self):
        s = Stack()
        self.assertEqual(True, s.isEmpty())

    def test_isEmpty_push1(self):
        s = Stack()
        s.push(5)
        self.assertEqual(False, s.isEmpty())

    def test_isEmpty_push1_pop1(self):
        s = Stack()
        s.push(1)
        s.pop()
        self.assertEqual(True, s.isEmpty())

    def test_peek_push1(self):
        s = Stack()
        s.push(88)
        self.assertEqual(88, s.peek())

    def test_peek_push3_pop1(self):
        s = Stack()
        s.push(7)
        s.push(889)
        s.push(3)
        s.pop()
        self.assertEqual(889, s.peek())

    def test_pop_empty(self):
        s = Stack()
        self.assertRaises(IndexError, s.pop)

    def test_peek_empty(self):
        s = Stack()
        self.assertRaises(IndexError, s.peek)

if __name__ == '__main__':
    unittest.main()




    