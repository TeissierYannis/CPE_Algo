class Table:

    def __init__(self, size, hash_method):
        """
        Init a table with a size and a hash method
        :param size: Number of slots in the table
        :param hash_method:  A hash method that takes a key and a size and returns an index
        :return: None
        """
        self.size = size
        self.hash_method = hash_method
        self.table = [None] * size

    def insert(self, key, value):
        """
        Insert a value into the table
        :param key: Position in the table
        :param value: Value to insert
        :return: None
        """
        index = self.hash_method(key, self.size)
        self.table[index] = value

    def delete(self, key):
        """
        Delete a value from the table
        :param key: Position in the table
        :return: Boolean
        """
        index = self.hash_method(key, self.size)
        if self.table[index] is None:
            return False
        self.table[index] = None
        return True

    def exist(self, key):
        """
        Check if a key exists in the table
        :param key: Position in the table
        :return: Boolean
        """
        index = self.hash_method(key, self.size)
        return self.table[index] is not None

    def value(self, key):
        """
        Get the value of a key
        :param key: Position in the table
        :return: Value
        """
        index = self.hash_method(key, self.size)
        return self.table[index]

    def union(self, other_table):
        """
        Union of two tables
        :param other_table: Table to union
        :return: Table
        """
        new_table = Table(self.size, self.hash_method)
        for i in range(self.size):
            if self.table[i] is not None:
                new_table.insert(i, self.table[i])
            if other_table.table[i] is not None:
                new_table.insert(i, other_table.table[i])
        return new_table

    def intersection(self, other_table):
        """
        Intersection of two tables
        :param other_table: Table to intersect
        :return: Table
        """
        new_table = Table(self.size, self.hash_method)
        for i in range(self.size):
            if self.table[i] is not None and other_table.table[i] is not None:
                new_table.insert(i, self.table[i])
        return new_table

    def display(self):
        """
        Display the table
        :return: None
        """
        print(self.table)