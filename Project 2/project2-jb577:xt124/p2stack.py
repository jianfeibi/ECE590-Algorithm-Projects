"""
Math 590
Project 2
Fall 2019

p2stack.py

Partner 1: Jianfei Bi
Partner 2: Xichen Tan
Date: 2019-11-06
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init_ function is a constructor.
    __init__ function to initialize the Stack.
    Note: initially the size of the stack defaults to 100.
    Note: the stack is initially filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=100):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.stack)
        print('Top: %d' % self.top)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        return self.numElems == len(self.stack)

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        return self.numElems == 0


    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        self.stack = self.stack + [None for x in range(0, len(self.stack))]
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        # If the stack is full, resizing is necessary
        # for a new value to be pushed.
        if self.isFull() is True:
            self.resize()

        # Put the new value at the right position
        # change top and numElems accordingly
        self.stack[self.numElems] = val
        self.top = self.top + 1
        self.numElems = self.numElems + 1

        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        if self.isEmpty() is True:
            raise Exception('This is an empty stack!')
            return None

        val = self.stack[self.top]
        self.stack[self.top] = None
        self.top = self.top - 1
        self.numElems = self.numElems - 1
        return val
