"""
Your task is create your own HashTable without using a built-in library.

Your HashTable needs to have the following functions:

- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.

Example:

```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.array = [None] * 20
        self.next = None

class MyHashTable:
    def __init__(self):
        # Your code here


    def put(self, key, value):
        # Your code here
        # Hash the key (map it to an integer in a finite space)
        hashed_key = hash(key)
        # Map the hashed ket to an index in the array by % len(array)
        index = hashed_key % len(self.array)
        # Put the value in the array at that index
        self.array[index] = value

    def get(self, key):
        # Your code here
        # PLAN: return the value at the index of the key
        # hash the key, map it to the index, and then return the value at that index in the array
        hashed_key = hash(key)
        index = hashed_key % len(self.array)
        if self.array[index] is None:
            return -1
        return self.array[index]
        return self.array[index]

    def remove(self, key: int) -> None:
        hashed_key = hash(key)
        index = hashed_key % len(self.array)

        self.array[index] = None
        # Your code here


hash_table = MyHashTable()
hash_table.put("a", 1)
hash_table.put("b", 2)
print(hash_table.get("a")) # returns 1
print(hash_table.get("b")) # returns 2
print(hash_table.get("3")) # returns -1 (not found)

hash_table.put("b", 1) # Update the existing value
print(hash_table.get("b")) # returns 1
hash_table.remove("b") # remove the mapping for 2
print(hash_table.get("b")) # returns - 1 (not found)


hash_table_2 = MyHashTable()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in alphabet:
    hash_table_2.put(c,c)

for c in alphabet:
    print(c, hash_table_2.get(char))