# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 2
# Term:        Fall 2017

import unittest
import stacks

class TestLab2(unittest.TestCase):

    # Tests list implementation

    def test_is_empty_1(self):
        stack = stacks.StackArray(10) #Creates empty stack
        self.assertTrue(stack.is_empty())

    def test_is_empty_2(self):
        stack = stacks.StackArray(10) #Creates empty stack
        stack.push(2) #Adds a value
        self.assertFalse(stack.is_empty())


    def test_is_full_1(self):
        stack = stacks.StackArray(10)  #Creates an empty stack
        self.assertFalse(stack.is_full())

    def test_is_full_2(self):
        stack = stacks.StackLinked(10) #Creates an empty stack
        for i in range(10):
            stack.push(i)    #Puts 10 values in the stack
        self.assertTrue(stack.is_full())


    def test_push_1(self):
        stack = stacks.StackArray(10)
        stack.push(25)     #Pushes a value onto the stack
        self.assertEqual(stack.size(), 1)

    def test_push_2(self):
        stack = stacks.StackArray(10)
        for i in range(10):
            stack.push(i)           #Fills the stack
        with self.assertRaises(IndexError): 
            stack.push(10)          #Checks for an error on next push


    def test_pop_1(self):
        stack = stacks.StackArray(10)
        stack.push(25)                  #Adds two elements to the stack
        stack.push(45)
        self.assertEqual(stack.pop(), 45)  #Removes the first, checks if the other is there
        self.assertEqual(stack.size(), 1)

    def test_pop_2(self):
        stack = stacks.StackArray(10)
        stack.push(25)                     #Adds one value
        self.assertEqual(stack.pop(), 25)  #Removes value and makes sure the stack is empty
        self.assertTrue(stack.is_empty())

    def test_pop_3(self):
        stack = stacks.StackArray(10)
        with self.assertRaises(IndexError): #Tries to pop an empty stack
            stack.pop()


    def test_peek_1(self):
        stack = stacks.StackArray(10)
        stack.push(45)                      #Adds a value
        self.assertEqual(stack.peek(), 45)  #Peeks at the value and makes sure it's still there
        self.assertEqual(stack.size(), 1)

    def test_peek_2(self):
        stack = stacks.StackArray(10)
        with self.assertRaises(IndexError): #Tries to peek an empty stack
            stack.peek()


    def test_size_1(self):
        stack = stacks.StackArray(10)
        for i in range(5):
            stack.push(i)                   #Adds 5 elements to the stack
        self.assertEqual(stack.size(), 5)   #Makes sure there are 5 elements

    def test_size_1(self):
        stack = stacks.StackArray(10)
        self.assertEqual(stack.size(), 0)   #Makes sure there is nothing in an empty stack



    # Tests linked list implementation
    # Tests are the same as above

    def test_linked_is_empty_1(self):
        stack = stacks.StackLinked(10)
        self.assertTrue(stack.is_empty())

    def test_linked_is_empty_2(self):
        stack = stacks.StackLinked(10)
        stack.push(2)
        self.assertFalse(stack.is_empty())


    def test_linked_is_full_1(self):
        stack = stacks.StackLinked(10)
        self.assertFalse(stack.is_full())

    def test_linked_is_full_2(self):
        stack = stacks.StackLinked(10)
        for i in range(10):
            stack.push(i)
        self.assertTrue(stack.is_full())


    def test_linked_push_1(self):
        stack = stacks.StackLinked(10)
        stack.push(25)
        self.assertEqual(stack.size(), 1)

    def test_linked_push_2(self):
        stack = stacks.StackLinked(10)
        for i in range(10):
            stack.push(i)
        with self.assertRaises(IndexError): 
            stack.push(10)


    def test_linked_pop_1(self):
        stack = stacks.StackLinked(10)
        stack.push(25)
        stack.push(45)
        self.assertEqual(stack.pop(), 45)
        self.assertEqual(stack.pop(), 25)

    def test_linked_pop_2(self):
        stack = stacks.StackLinked(10)
        stack.push(25)
        self.assertEqual(stack.pop(), 25)
        self.assertTrue(stack.is_empty())

    def test_linked_pop_3(self):
        stack = stacks.StackLinked(10)
        with self.assertRaises(IndexError): 
            stack.pop()


    def test_linked_peek_1(self):
        stack = stacks.StackLinked(10)
        stack.push(45)
        self.assertEqual(stack.peek(), 45)
        self.assertEqual(stack.size(), 1)

    def test_linked_peek_2(self):
        stack = stacks.StackLinked(10)
        with self.assertRaises(IndexError): 
            stack.peek()


    def test_linked_size_1(self):
        stack = stacks.StackLinked(10)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.size(), 5)

    def test_linked_size_1(self):
        stack = stacks.StackLinked(10)
        self.assertEqual(stack.size(), 0)



if __name__ == "__main__":
        unittest.main()
