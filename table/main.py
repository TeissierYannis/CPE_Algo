# Main.py

import Table

if __name__ == '__main__':
    # Create a table with 10 positions and the hash method

    # Create a hash method for the hash table
    def hash_method(key, size):
        return key % size

    table = Table.Table(10, hash_method)

    for i in range(10):
        table.insert(i, i)

    table.display()