# Your HashMap class definition (including the corrected 'insert' method)
class HashMap:
    def __init__(self) -> None:
        self.size = 100
        self.data = [None for _ in range(self.size)]

    def get_hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, val):
        h = self.get_hash(key)
        if self.data[h] is None:
            self.data[h] = [(key, val)]
        else:
            self.data[h].append((key, val))

    def get(self, key):
        h = self.get_hash(key)
        if self.data[h] is not None:
            for k, v in self.data[h]:
                if k == key:
                    return v
            return None

    def located(self, key):
        for i, bucket in enumerate(self.data):
            if bucket is not None:
                for k, _ in bucket:
                    if k == key:
                        return i
        return None
    
    def delete(self, key):
        h = self.get_hash(key)
        if self.data[h] is not None:
            for i, (k, v) in enumerate(self.data[h]):
                if k == key:
                    del self.data[h][i]
                    return
        return 'Not found'

    def update_key(self, key, new_key):
        h = self.get_hash(key)
        if self.data[h] is not None:
            for i, (k, v) in enumerate(self.data[h]):
                if k == key:
                    self.data[h][i] = (new_key, v)
                    break

    def update_val(self, key, new_val):
        h = self.get_hash(key)
        if self.data[h] is not None:
            for i, (k, v) in enumerate(self.data[h]):
                if k == key:
                    self.data[h][i] = (k, new_val)
                    break
    def clear(self):
        return self.data == None
    
    def get_keys(self):
        result = []
        for bucket in self.data:
            if bucket is not None:
                for key, _ in bucket:
                    result.append(key)
        return result

    def get_vals(self):
        result = []
        for bucket in self.data:
            if bucket is not None:
                for _, val in bucket:
                    result.append(val)
        return result

    def resize(self, new_size):
        old_data = self.data
        self.size = new_size
        self.data = [None for _ in range(self.size)]
        for bucket in old_data:
            if bucket is not None:
                for key, val in bucket:
                    self.insert(key, val)
            

        

# Assuming your HashMap class is defined with the update_key and update_val methods

# Create a HashMap
hash_map = HashMap()

# Insert some key-value pairs
hash_map.insert('apple', 10)
hash_map.insert('banana', 20)
hash_map.insert('cherry', 30)

# Display the hash map before updates
for i, bucket in enumerate(hash_map.data):
    print(f'Bucket {i}: {bucket}')

# Update the key for 'banana' to 'grape'
hash_map.update_key('banana', 'grape')

# Update the value for 'cherry' to 35
hash_map.update_val('cherry', 35)

# Display the hash map after updates
print("\nAfter Updates:")
for i, bucket in enumerate(hash_map.data):
    print(f'Bucket {i}: {bucket}')

# Retrieve values after updates
print("\nValues after Updates:")
print("Value of 'banana':", hash_map.get('banana'))  # Output: Value of 'banana': None (key updated)
print("Value of 'cherry':", hash_map.get('cherry'))  # Output: Value of 'cherry': 35
print("Value of 'grape':", hash_map.get('grape'))    # Output: Value of 'grape': 20 (value not updated)
