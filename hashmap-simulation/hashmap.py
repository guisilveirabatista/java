# This script simulates the core behavior of a Java HashMap.
# It provides a step-by-step textual "visualization" of how
# key-value pairs are stored and retrieved, especially how
# collisions are handled.

class HashMapSimulation:
    def __init__(self, size=16):
        """
        Initializes the hash map with a specified size.
        The underlying data structure is a list of lists,
        where each inner list represents a "bucket" and
        stores key-value pairs as tuples.
        """
        self.size = size
        self.table = [None] * self.size

    def _hash_function(self, key):
        """
        A simple hash function that simulates Java's `hashCode()`
        and modulo operation to determine the bucket index.
        """
        # The built-in hash() function in Python is similar to Java's hashCode().
        # The modulo operator ensures the index fits within the table's size.
        return hash(key) % self.size

    def put(self, key, value):
        """
        Adds a new key-value pair to the hash map.
        This method demonstrates how new entries are placed and
        how collisions are resolved by appending to a list (simulating
        a linked list of entries).
        """
        print(f"--> Putting '{key}': '{value}'")
        index = self._hash_function(key)
        
        # Scenario 1: No collision. The bucket is empty.
        if self.table[index] is None:
            self.table[index] = [(key, value)]
            print(f"    - No collision. Stored at bucket: {index}")
        # Scenario 2: Collision detected.
        else:
            print(f"    - Collision detected at bucket: {index}")
            found = False
            # Iterate through the bucket's list to check if the key already exists.
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # If the key exists, update the value.
                    self.table[index][i] = (key, value)
                    print(f"    - Key '{key}' already exists. Value updated.")
                    found = True
                    break
            # If the key is new, append the new entry to the end of the list.
            if not found:
                self.table[index].append((key, value))
                print(f"    - New entry appended to the list (simulating linked list).")

        print("Current HashMap state:")
        self.print_table()
        print("-" * 40)

    def get(self, key):
        """
        Retrieves a value based on a given key.
        This demonstrates the speed of lookup by directly going to the
        correct bucket before searching the contained list.
        """
        print(f"--> Getting value for key '{key}'")
        index = self._hash_function(key)
        
        # Check if the bucket at the calculated index is not empty.
        if self.table[index] is not None:
            # Iterate through the list in the bucket to find the matching key.
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    print(f"    - Found value '{value}' at bucket: {index}")
                    print("-" * 40)
                    return value
        
        print(f"    - Key '{key}' not found.")
        print("-" * 40)
        return None

    def print_table(self):
        """
        Utility function to print the current state of the entire hash table.
        This is the "visual" part of the simulation.
        """
        for i, bucket in enumerate(self.table):
            # Print the bucket index and its contents.
            print(f"Bucket {i:2d}: {bucket}")

# --- Example Usage ---
# Create a simulated HashMap with a small size to force collisions and make
# the visualization clearer. A real HashMap is usually much larger.
hm = HashMapSimulation(size=5)

# 1. Add some entries.
hm.put("apple", 10)
hm.put("banana", 20)
hm.put("cherry", 30)

# 2. Add an entry that will likely cause a collision.
# The hash of "grape" will map to the same bucket as "apple" or "banana"
# because the table size is small (5).
hm.put("grape", 40)

# 3. Update an existing entry.
hm.put("apple", 100)

# 4. Retrieve values.
hm.get("banana")
hm.get("grape")
hm.get("pineapple") # This key does not exist
