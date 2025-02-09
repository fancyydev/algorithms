
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
            #print("APPEND PROCESS----------------------")
            
            while node.get_next() != None:
                #print(node.get_value())
                node = node.get_next()
            
            #print(node.get_value())
            node.set_next(new_node)
            #print(node.get_next().get_value())
            self.tail = new_node
            #print("--------------------------")
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
        #This function allows us to delete a node using an index or an specific node or a value
        count = 1
        succesfull_delete = False
        if self.head!=None:
                
            node = self.head
            params = [index, node_old, node_value]
            if sum(param is not None for param in params) > 1:
                print("You can delete a node using either an index, a node value, or a specific node, but not more than one at the same time.")
            
            else:
                if index != None:
                    # Podria cambiarlo para mejorar la coherencia del codigo con el de node_old
                    # If the head and tail is the node that i want to remove
                    if index == 0 and node.get_next() == None:
                        self.head = None
                        self.tail = None
                    else:
                        # If the head is the node that i want to remove
                        if index == 0:
                            self.head = self.head.get_next()
                            succesfull_delete = True
                        else:
                            # We look for the previous node that points to the index
                            while count != index and node.get_next() != None:
                                node = node.get_next()
                                count += 1
                                
                            node_old = node.get_next()
                            # if we find the right node in the right position, we delete it.
                            if count == index:
                                node.set_next(node_old.get_next())
                                if node_old == self.tail:
                                    self.tail = node
                                succesfull_delete = True
                                
                elif node_old != None:
                    # If the head is the node that i want to remove
                    if node_old == self.head:
                        if self.tail != self.head:
                            self.head = self.head.get_next()
                            succesfull_delete = True
                        else:
                            # If we want delete the unique node that we have
                            # If we want to remove the only node we have (correct)
                            self.head = None
                            self.tail = None
                    else:  
                        # If the next node of node is the node_old that i want to remove
                        # I change the pointer of node to the pointer of node_old 
                        # And if node_old is tail i change the pointer tail to node
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
                        # If the head has the value that i want to remove
                        if self.head.get_value() == node_value:
                            if self.tail != self.head:
                                self.head = self.head.get_next()
                                succesfull_delete = True
                            else:
                                self.head = None
                                self.tail = None
                        else: 
                            
                            # We have to find the node that points to another node with the value we are looking for
                            while node.get_next().get_value() != node_value and node.get_next() != None:
                                node = node.get_next()
                            
                        
                            node_old = node.get_next()
                            # If the next node of node has the value that i want to remove
                            # I change the pointer of node to the pointer of node_old 
                            # And if node_old is tail i change the pointer tail to node
                            if node_old.get_value() == node_value:
                                node.set_next(node_old.get_next())
                                if node_old == self.tail:
                                    self.tail = node
                                succesfull_delete = True
                    except: 
                        print("I cant find the value to delete")
        else:
            print("The linked list is empty")
                    
    def insert(self, index = None, previous_node = None, value = None, new_node = None):
        count = 1
        node = self.head
        if self.head != None:
            
            params = [index, previous_node, value]
            
            if(sum(param is not None for param in params) > 1):
                print("You can insert a node using either an index, a node value, or a specific node, but not more than one at the same time.")
            else:
                if index!=None:
                    if index == 0:
                        new_node.set_next(node)
                        self.head = new_node
                    else:
                        while(index != count and node.get_next() != None):
                            node = node.get_next()
                            count += 1
                        
                        if node != self.tail:
                            next_node = node.get_next()
                        
                            if (index == count):
                                new_node.set_next(next_node)
                                node.set_next(new_node)        
                        else:
                            if (index == count):
                                node.set_next(new_node)
                                self.tail = new_node
                                                            
                elif previous_node != None:
                    if previous_node == self.head:
                        new_node.set_next(self.head.get_next())
                        self.head.set_next(new_node)
                    else:
                        while(node != previous_node and node.get_next() != None):
                            node = node.get_next()
                            
                        if node != self.tail:
                            if (node == previous_node):
                                new_node.set_next(node.get_next())
                                node.set_next(new_node)     
                        else:
                            if (node == previous_node):
                                node.set_next(new_node)
                                self.tail = new_node
                                
                elif value != None:
                    if value == self.head.get_value():
                        new_node.set_next(self.head.get_next())
                        self.head.set_next(new_node)
                    else:
                        while(node.get_value() != value and node.get_next() != None):
                            node = node.get_next()
                        if node != self.tail:
                            if (node.get_value() == value):
                                new_node.set_next(node.get_next())
                                node.set_next(new_node)     
                        else:
                            if (node.get_value() == value):
                                node.set_next(new_node)
                                self.tail = new_node
                    
        else:
            print("The linked list is empty")
        
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
node5 = Node(5)
ll = LinkedList(head)
ll.append(node2)
ll.append(node3)

ll.insert(index=3, new_node=node5)
ll.insert(previous_node=node5, new_node=Node(45))
ll.insert(value=3, new_node=Node(55))
ll.road()

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

# ll.delete(index=1)
# print("--------------------")
# ll.road()

# ll.delete(index=1)
# print("--------------------")
# ll.road()

# ll.delete(index=0)
# print("--------------------")
# ll.road()
# # ll.delete(node_value=5)
# print("--------------------")
# ll.road()