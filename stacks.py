# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 2
# Term:        Fall 2017

class StackArray:
    
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity= capacity
        self.items = [None] * capacity
        self.num_items = 0 

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return (self.num_items == 0)
 
    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return (self.num_items == self.capacity)
 
    def push(self, item):
        """Adds to the top of the stack"""
        if self.is_full():
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1
 
    def pop(self):
        """Removes the last thing on the stack"""
        if self.is_empty():
            raise IndexError
        value = self.items[self.num_items - 1]
        self.items[self.num_items - 1] = None
        self.num_items -= 1
        return value
 
    def peek(self):
        """Returns item on the top of the stack but does not remove it"""
        if self.is_empty():
            raise IndexError
        return self.items[self.num_items - 1]

    def size(self):
       """Returns the number of items in the stack"""
       return self.num_items



class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next



class StackLinked:

    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return (self.head == None)
 
    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return (self.size() == self.capacity)
 
    def push(self, item):
        """Adds values to the stack"""
        if self.is_full():
            raise IndexError
        new_next = self.head
        self.head = Node(item)
        self.head.set_next(new_next)
 
    def pop(self):
        """Removes the last thing that went into the stack"""
        if self.is_empty():
            raise IndexError
        popped = self.head.get_data()
        self.head = self.head.get_next()
        return popped

    def peek(self):
        """Returns item on the top of the stack but does not remove it"""
        if self.is_empty():
            raise IndexError
        return self.head.get_data()

    def size(self):
       """Returns the number of items in the stack"""
       num_items = 0
       current = self.head
       while current != None:
           num_items += 1
           current = current.next
       return num_items
