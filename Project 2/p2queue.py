"""
Math 590
Project 2
Fall 2019

p2queue.py

Partner 1: Jianfei Bi
Partner 2: Xichen Tan
Date: 2019-11-06
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: initially the size of the queue defaults to 100.
    Note: the queue is initially filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.queue)
        print('Front: %d' % self.front)
        print('Rear: %d' % self.rear)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        return self.numElems == len(self.queue)
    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        return self.numElems == 0

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        # Use temp to store the original queue,
        # then expand self.queue to twice the size
        temp = self.queue.copy()
        self.queue = [None for x in self.queue] * 2

        _front = self.front
        # Rearrange and copy the original data to the
        # new queue.
        for k in range(0, self.numElems):
            self.queue[k] = temp[_front]
            _front = (1 + _front) % len(temp)

        # Reset front and rear to the right spots.
        self.front = 0
        self.rear = self.numElems
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        # If queue is full, resizing is needed for pushing in
        # a new element.
        if self.isFull() is True:
            self.resize()

        self.queue[self.rear] = val
        self.numElems = self.numElems + 1
        self.rear = (self.rear + 1) % len(self.queue)
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        if self.isEmpty() is True:
            raise Exception('This is an empty queue!')
            return None
        # (Some random note..)
        # There is no need to reset the popped value
        # because it will be overwritten at some point anyway.
        # If we are storing objects instead of integers in the queue,
        # then we should reset it to None for storage purposes.
        temp = self.queue[self.front]
        self.front = (self.front + 1) % len(self.queue)
        self.numElems = self.numElems - 1

        return temp
