class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert_val(self, key, val):

        hashed_key = hash(key) % self.size
        hashed_list = self.table[hashed_key]

        found_key = False
        for idx, item in enumerate(hashed_list):
            recorded_key, _ = item
            if recorded_key == key:
                found_key = True
                break

        if found_key:
            hashed_list[idx] = (key,val)
        else:
            hashed_list.append((key,val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        hashed_list = self.table[hashed_key]

        found_key = False
        for idx, item in enumerate(hashed_list):
            recorded_key, recorded_val = item
            if recorded_key == key:
                found_key = True
                break
        
        if found_key:
            return recorded_val
        else:
            return None

    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        hashed_list = self.table[hashed_key]

        for idx, item in enumerate(hashed_list):
            recorded_key, _ = item
            if recorded_key == key:
                hashed_list.pop(idx)
                break

    def __str__(self): 
        return "".join(str(item) for item in self.table) 

if __name__ == '__main__':
    hash_table = HashTable(10)
    print(hash_table)

    # insert some values 
    hash_table.insert_val('Alvin', 30) 
    print(hash_table) 
    print() 
    
    hash_table.insert_val('tom', 12) 
    print(hash_table) 
    print() 
    
    # search/access a record with key 
    print(hash_table.get_val('Alvin')) 
    print() 
    
    # delete or remove a value 
    hash_table.delete_val('tom') 
    print(hash_table) 