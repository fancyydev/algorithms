#First in first out

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value = None):
        if value is not None:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.lenght = 1 
        else:
            self.first = None
            self.last = None
            self.lenght = 0
            
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def enqueue(self, value):
        new_node = Node(value)
        if self.lenght != 0:
            self.last.next = new_node
            self.last = new_node
        else:
            self.first = new_node
            self.last = new_node
        self.lenght += 1
        
    def dequeue(self):
        if self.lenght > 0:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.lenght -= 1
        else:
            print("Your queue is empty")
    
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.dequeue()


my_queue.print_queue()

