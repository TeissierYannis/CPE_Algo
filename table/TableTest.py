# TableTest.py

import unittest

from Table import Table

class TestTable(unittest.TestCase):
    def test_insert(self):
        table = Table(5, lambda key, size: key % size, lambda key, size: (key + 1) % size)
        index_val_1 = table.insert(0, 'value1')
        index_val_2 = table.insert(5, 'value2')
        self.assertEqual(table.value(index_val_1), 'value1')
        self.assertEqual(table.value(index_val_2), 'value2')
        self.assertTrue(table.exist(index_val_1))
        self.assertTrue(table.exist(index_val_2))

    def test_delete(self):
        table = Table(5, lambda key, size: key % size, lambda key, size: (key + 1) % size)
        index_val_1 = table.insert(0, 'value1')
        self.assertTrue(table.exist(index_val_1))
        self.assertTrue(table.delete(index_val_1))
        self.assertFalse(table.exist(index_val_1))
        self.assertFalse(table.delete(index_val_1))

    def test_union(self):
        table1 = Table(5, lambda key, size: key % size, lambda key, size: (key + 1) % size)
        index_val_1 = table1.insert(0, 'value1')
        table2 = Table(5, lambda key, size: key % size, lambda key, size: (key + 1) % size)
        index_val_2 = table2.insert(1, 'value2')
        index_val_1_t2 = table2.insert(0, 'value1')
        table3 = table1.union(table2)
        self.assertTrue(table3.exist(index_val_1))
        self.assertTrue(table3.exist(index_val_2))

    def test_intersection(self):
        table1 = Table(5, lambda key, size: key % size, lambda key, size: (key + 1) % size)
        index_val_1 = table1.insert(0, 'value1')
        index_val_2 = table1.insert(1, 'value2')
        table2 = Table(5, lambda key, size: key % size, lambda key, size: (key + 1) % size)
        index_val_3 = table2.insert(0, 'value1')
        index_val_4 = table2.insert(2, 'value4')
        table3 = table1.intersection(table2)

        self.assertTrue(table3.exist(index_val_1))
        self.assertFalse(table3.exist(index_val_2))
        self.assertTrue(table3.exist(index_val_3))
        self.assertFalse(table3.exist(index_val_4))


if __name__ == '__main__':
    unittest.main()