# Los parentesis dentro de una clase se usan para definir herencia
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value = None):
        if value != None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            #Este atributo nos sirve para saber la longitud de nuestra linked list
            self.length = 1
        else:
            self.head = value
            self.tail = value
            self.length = 0    
    
    def append(self, value):
        new_node = Node(value)
        if (self.length > 0):
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        
        return True
    
    def pop(self):
        temp = self.head
        if self.length > 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                while temp.next != self.tail and temp.next != None:
                    temp = temp.next
        
                temp.next = None
                self.tail = temp
                
            self.length -= 1
        else:
            print("This is an empty linked list")
    
    def delete(self, value):
        temp = self.head
        if self.length > 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                while temp.next.value != value and temp.next != None:
                    temp = temp.next
                
                if temp.next.value == value:
                    if temp.next == self.tail:
                        temp.next = None
                        self.tail = temp
                    else:
                        temp.next = temp.next.next
            self.length -= 1
        else:
            print("This is an empty linked list")
        
    def prepend(self, value):
        print()
    
    def insert(self, index, value):
        print()
    
    def print_list(self):
        if self.length > 0:
            temp = self.head
            while(temp is not None):
                print(temp.value)
                temp = temp.next
        else:
            print("This is an empty list")
            
my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(5)

# my_linked_list.delete(5)
# my_linked_list.delete(2)
# my_linked_list.delete(1)

my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()


my_linked_list.print_list()