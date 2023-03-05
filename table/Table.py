class Table:

    def __init__(self, size, hash_method, rehash_method):
        """
        Init a table with a size and a hash method
        :param size: Number of slots in the table
        :param hash_method:  A hash method that takes a key and a size and returns an index
        :return: None
        """
        self.size = size
        self.hash_method = hash_method
        self.table = [None] * size
        self.rehash_method = rehash_method
        self.count = 0

    def insert(self, key, value):
        """
        Insert a value into the table
        :param key: Position in the table
        :param value: Value to insert
        :return: index: Index of the value
        """
        if self._is_table_full():
            raise Exception('Table is full')
        index = self.hash_method(key, self.size)
        # If the slot is not empty, we do not insert the value
        if self.table[index] is None:
            self.table[index] = value
        else:
            index = self._rehash_until_filled(key)
            self.table[index] = value
        self.count += 1
        return index

    def _rehash_until_filled(self, key):
        """
        Rehash until the slot is filled
        :param key: Position in the table
        :param value: Value to insert
        :return: index: Index of the value
        """
        # Rehash method take the key, the number of iteration and the size of the table
        iteration = 0
        index = self.rehash_method(key, iteration, self.size)
        while self.table[index] is not None and not self._is_table_full():
            index = self.rehash_method(index, iteration, self.size)
            iteration += 1
        return index

    def _is_table_full(self):
        """
        Check if the table is full
        :return: Boolean
        """
        return self.count == self.size

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
        if self.table[index] is None:
            index = self._rehash_until_filled(key)
            if self.table[index] is None:
                return False
        return True

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
        new_table = Table(self.size, self.hash_method, self.rehash_method)
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
        new_table = Table(self.size, self.hash_method, self.rehash_method)
        for i in range(self.size):
            if self.table[i] is not None and other_table.table[i] is not None:
                new_table.insert(i, self.table[i])
        return new_table
