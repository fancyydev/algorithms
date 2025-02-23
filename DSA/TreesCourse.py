# BINARY TREE
# In a complete tree, each node points to two other nodes
# In a perfect tree, each node at one level points to two other nodes
# In a complete tree, each node at one level excluding the last one points to two other nodes, 
# and at the last level the nodes have a left-handed order

# Concepts
# Parent: In a tree, each node can have only one parent.
# Child: If a node is pointed to by another node, it is a child.
# Leaf: If a node does not have any children, it is a leaf.
# Aproximate number of nodes 2^n -1 where n = the number of levels

# BINARY SEARCH TREE
# In a Binary Search Tree (BST), nodes must be arranged based on their values. 
# If a new value is greater than the parent, it becomes the right child; otherwise, it becomes the left child.

# Big O
# Search: O(log n) is basically the same principle of divide and conquer - O(n) in the worst scenario
# Insert: O(log n)
# Remove: O(log n)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self, value = None):
        
        if value is not None:
            new_node = Node(value)
            self.root = new_node
            self.level = 1
        else:
            self.root = None
            self.level = 0
        # Tal vez podriamos usar niveles
        # Tal vez podriamos usar cantidad de nodos
        
    def print_tree(self):
        def _in_order_traversal(node):
            if node is not None:
                _in_order_traversal(node.left)  # Recorre el subárbol izquierdo
                print(node.value, end=" ")  # Imprime el nodo actual
                _in_order_traversal(node.right)  # Recorre el subárbol derecho
        
        _in_order_traversal(self.root)
        print() 
        
    def insert(self, value):
        new_node = Node(value)
        temp = self.root
        
        while True:
            if self.root is None:
                self.root = new_node
                break
            
            if temp.value == new_node.value:
                return False
            
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left
    
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
                
        return False        

        
    def delete(self):
        print()

bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

print(bst.contains(3))
bst.print_tree()