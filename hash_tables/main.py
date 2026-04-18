

# In a hash table we should always have a prime number of memory
# locations for the key, value pairs. This will increase the randomness
# of assignments and reduces collisions.



class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash       
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []

        self.data_map[index].append([key, value])    

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None        



    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    


table = HashTable() 
table.set_item('bolts', 1400)
table.set_item('washers', 50)
table.set_item('lumber', 70) 
table.set_item('tyler', 33) 
table.print_table() 
print(table.get_item('tyler'))

