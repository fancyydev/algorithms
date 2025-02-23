# Address space
# A hash table is a data structure that stores data using keys and
# values in conjunction with a hash method to save this data efficiently.

# Hash it is in one way value -> addres addres !=> value
# It is deterministic: for a particula hash function every time we put a 
# specific value we expect the same specific address

# This is a list with in a list

# The technique of dealing with collisions, where you just put them at the same addres is called 
# Separate chaining
# Other techinque of dealing with collisions is go down until you find an empty address
# Linear probing open addressing this makes it where you dont have more than one key value pair at any address

# For any integer N divided by an integer M, the remainder is always in the range 0 ≤ remainder < M.

#This can be useful to find repited numbers in two different lists

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None]*size
    
    # This is the hash method to get a index number using the key
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    # O(1) +
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    # O(n)
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return False
    
    # O(n^2)
    def get_keys(self):
        all_keys = []
        for array in self.data_map:
            if array is not None:
                for items in array:
                    all_keys.append(items[0])
        return all_keys
                
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    
    
my_hash_table = HashTable()

my_hash_table.set_item('mamalon', 5000)
my_hash_table.set_item('perroni', 3000)
my_hash_table.set_item('perron', 2000)

print(my_hash_table.get_item('quiensabe'))
print(my_hash_table.get_item('mamalon'))
print(my_hash_table.get_item('perron'))
print(my_hash_table.get_item('perroni'))

#my_hash_table.print_table()
print(my_hash_table.get_keys())    