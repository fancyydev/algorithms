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
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
        self.level = 1
        # Tal vez podriamos usar niveles
        # Tal vez podriamos usar cantidad de nodos
    def print_tree(self):
        print()
    def append(self):
        print()
    def delete(self):
        print()
        
for i in range(4):
    print(i)