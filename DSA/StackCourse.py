# Last in first off
# We can use a list and only add or remove from the same in
# The time complexity of add or remove from the last in is O(1)
# The time complexity of add or remove from the begining of the list is O(n)

# We can also create a stack using a linked list, and we can perform the 
# following operations more efficiently by using the head



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value = None):
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0
        
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.height != 0:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
        self.height += 1 
        
    def pop(self):
        # I need include this in my program of linked list to clean the next value
        if self.height > 0:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1 
        else:
            print("Your stack is empty")
        
my_stack = Stack()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.pop()
my_stack.pop()
my_stack.pop()

my_stack.print_stack()


    
         
        
