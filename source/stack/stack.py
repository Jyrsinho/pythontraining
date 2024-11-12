"""
Class for basic stack.

Author: Jyri Huhtala
Date: 2024-12-11
"""


class Stack:
    
    
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.elements = [0] * capacity
        
    
    
    def push(self, item):
        """
        adds given element to the top of the stack and increases the size of the stack by one. If the stack is full, 
        capacity of the stack will be doubled.
        :param item: element to be added
        """
        if self.size == self.capacity:
            self.expand_stack()
        
        self.elements[self.size] = item
        self.size += 1
    
        
    
    def top(self):
        """
        returns the top element of the stack
        :return: top element of the stack
        """
        return self.elements[self.size-1]



    def pop(self):
        """
        removes the top element from the stack and returns it
        :return: top element of the stack
        """
        if self.size == 0:
            print("Cannot pop an empty stack")
            return
        
        element_removed = self.elements[self.size-1]
        self.elements[self.size - 1] = 0
        self.size -= 1
        
        
        return element_removed
    
    
    def size(self):
        """
        returns the size of the stack
        :return: size of the stack
        """
        return self.size


    def is_empty(self):
        """
        checks if the stack is empty
        :return: true if the stack is empty, false otherwise
        """
        return self.size == 0
    
    
    def expand_stack(self):
        """
        Create new twice larger stack and copy all the old stack's elements
        to it
        """
        # create new stack with twice the capacity of the old stack
        self.capacity = self.capacity * 2
        new_stack = Stack(self.capacity)
        
        # copy all the elements from the old stack to the new stack
        for i in range(len(self.elements)):
            new_stack.push(self.elements[i])
        
        # replace old elements stack with new larger stack
        self.elements = new_stack.elements



def main():
    
    print ("Testing push- function:")
    print ("Created new stack with the capacity of 3")
    stack = Stack(3)
    print ("The size of the stack is " + str(stack.size))
    print("Executed stack.push(1)")
    stack.push(1)
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("The capacity of the stack is " + str(stack.capacity))
    print("Executed stack.push(2)")
    stack.push(2)
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("The capacity of the stack is " + str(stack.capacity))
    print("Executed stack.push(3)")
    stack.push(3)
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("The capacity of the stack is " + str(stack.capacity))
    print("Executed stack.push(4)")
    stack.push(4)
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("The capacity of the stack is " + str(stack.capacity))
    
    
    print()
    print ("Testing pop- function:")
    print ("The size of the stack is " + str(stack.size))
    print ("The top element of the stack is " + str(stack.top()))
    print("Executed stack.pop()")
    stack.pop()
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("Executed stack.pop()")
    stack.pop()
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("Executed stack.pop()")
    stack.pop()
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("Executed stack.pop()")
    stack.pop()
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("Executed stack.pop()")
    stack.pop()
    print("The size of the stack is " + str(stack.size))
    print("The top element of the stack is " + str(stack.top()))
    print("Executed stack.pop()")
    
    print ()
    print("Testing is empty-function")
    print("Executing stack.is_empty()")
    print ("Result of the function is:" + str(stack.is_empty()))
    print("Executed stack.push(1)")
    stack.push(1)
    print("Executing stack.is_empty()")
    print ("Result of the function is:" + str(stack.is_empty()))    
    

if __name__ == "__main__":
    main()