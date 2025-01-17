
class LinkedList():
    def __init__(self, initial_node):
        self.head = initial_node
        self.tail = initial_node
        
    def get_head(self):
        return self.head
    def set_head(self, head):
        if self.head != None:
            self.head = head
        else:
            print("The linked list is empty")
        
    def get_tail(self):
        return self.tail
    def set_tail(self, tail):
        if self.head != None:
            self.tail = tail
        else:
            print("The linked list is empty")
        
        
    def append(self, new_node):
        if self.head != None:
            node = self.head
            print("APPEND PROCESS----------------------")
            
            while node.get_next() != None:
                print(node.get_value())
                node = node.get_next()
            
            print(node.get_value())
            node.set_next(new_node)
            print(node.get_next().get_value())
            self.tail = new_node
            print("--------------------------")
        else:
            print("The linked list is empty")
            
    def pop(self):
        if self.head != None:
            node = self.head
            try:
                while node.get_next() != self.tail:
                    node = node.get_next()
                
                self.tail = node
                node.set_next(None)
            except AttributeError:
                print("You can not delete the unique node that you have")    
        else:
            print("The linked list is empty")
            
    def delete(self, index = None, node_old = None, node_value = None):
        count = 1
        succesfull_delete = False
        if self.head!=None:
                
            node = self.head
            params = [index, node_old, node_value]
            if sum(param is not None for param in params) > 1:
                print("You can delete a node using either an index, a node value, or a specific node, but not more than one at the same time.")
            
            else:
                if index != None:
                    if index == 0 and node.get_next() == None:
                        self.head = None
                        self.tail = None
                    else:
                        if index == 0:
                            self.head = self.head.get_next()
                            succesfull_delete = True
                        else:
                            while count != index and node.get_next() != None:
                                node = node.get_next()
                                count += 1
                                
                            node_old = node.get_next()
                            
                            if count == index:
                                node.set_next(node_old.get_next())
                                if node_old == self.tail:
                                    self.tail = node
                                succesfull_delete = True
                                
                elif node_old != None:
                    if node_old == self.head:
                        if self.tail != self.head:
                            self.head = self.head.get_next()
                            succesfull_delete = True
                        else:
                            self.head = None
                            self.tail = None
                    else:      
                        while node.get_next() != None:
                            if node.get_next() == node_old:
                                node.set_next(node_old.get_next())
                                if node_old == self.tail:
                                    self.tail = node
                                succesfull_delete = True
                            else: 
                                node = node.get_next()
                else:
                    try:
                        if self.head.get_value() == node_value:
                            if self.tail != self.head:
                                self.head = self.head.get_next()
                                succesfull_delete = True
                            else:
                                self.head = None
                                self.tail = None
                        else:  
                            while node.get_next().get_value() != node_value and node.get_next() != None:
                                node = node.get_next()
                            
                            node_old = node.get_next()
                            
                            if node_old.get_value() == node_value:
                                node.set_next(node_old.get_next())
                                if node_old == self.tail:
                                    self.tail = node
                                succesfull_delete = True
                    except: 
                        print("No se encontro el valor a eliminar")
        else:
            print("The linked list is empty")
                    
    def insert(self, index, node, new_node):
        print()
        
    def search(self, search_node):
        if self.head != None:
                
            node = self.head
            while node.get_value() != search_node and node.get_next() != None:
                node = node.get_next()
            
            if node.get_value() == search_node:
                return node
            else:
                return None
        else:
            print("The linked list is empty")        
            
    def road(self):
        if self.head != None:
            node = self.head
            print(node.get_value())
            
            while(node.get_next() != None):
                node = node.get_next()
                print(node.get_value())
        else:
            print("the linked list is empty")
            
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
        
    def get_next(self):
        return self.next
    def set_next(self, next):
        self.next = next

head = Node(1)
node2 = Node(2)
node3 = Node(3)
ll = LinkedList(head)
ll.append(node2)
ll.append(node3)

# search = ll.search(3)
# # print(search.get_value())

# ll.delete(node_old=head)
# print("--------------------")
# ll.road()

# # print(ll.get_head().get_value())
# # print(ll.get_tail().get_value())
# print("--------------------")
# ll.delete(node_old=node2)
# ll.road()

# print("--------------------")
# ll.delete(node_old=node3)
# ll.road()

# print(ll.get_head().get_value())
# print(ll.get_tail().get_value())

ll.delete(index=1)
print("--------------------")
ll.road()

ll.delete(index=1)
print("--------------------")
ll.road()

ll.delete(index=0)
print("--------------------")
ll.road()
# ll.delete(node_value=5)
# print("--------------------")
# ll.road()