import os
import random
import time
import unittest

from io import StringIO
import sys

# Import plot to draw graphs
import matplotlib.pyplot as plt


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ABR:
    def __init__(self):
        self.visited = None
        self.root = None

    def get_visited(self):
        """ Get the number of visited nodes
            :return: the number of visited nodes
        """
        return self.visited

    def insert(self, value):
        """ Insert a value in the tree
            If the value already exist in the tree, do nothing
            :param value: the value to insert
        """
        # If the root is None, the new value is set as the root node
        if self.root is None:
            self.root = Node(value)
        else:
            # Otherwise, the current node is set to the root node
            current = self.root
            while True:
                if value == current.value:
                    # If the value is already present in the tree, do nothing
                    return
                elif value < current.value:
                    if current.left is None:
                        # If the left child is None, create a new node with the value as the value and
                        # set it as the left child of the current node
                        current.left = Node(value)
                        return
                    else:
                        # Otherwise, the current node is set to the left child
                        current = current.left
                else:
                    if current.right is None:
                        # If the right child is None, create a new node with the value as the value and
                        # set it as the right child of the current node
                        current.right = Node(value)
                        return
                    else:
                        # Otherwise, the current node is set to the right child
                        current = current.right

    def delete(self, value):
        """ Delete a value in the tree
            If the value doesn't exist in the tree, do nothing
            :param value: the value to delete
        """
        if self.root is None:
            return
        else:
            current = self.root
            parent = None
            while True:
                if value == current.value:
                    if current.left is None and current.right is None:
                        if parent is None:
                            self.root = None
                        else:
                            if parent.left == current:
                                parent.left = None
                            else:
                                parent.right = None
                    elif current.left is None:
                        if parent is None:
                            self.root = current.right
                        else:
                            if parent.left == current:
                                parent.left = current.right
                            else:
                                parent.right = current.right
                    elif current.right is None:
                        if parent is None:
                            self.root = current.left
                        else:
                            if parent.left == current:
                                parent.left = current.left
                            else:
                                parent.right = current.left
                    else:
                        tmp = current.right
                        while tmp.left is not None:
                            tmp = tmp.left
                        current.value = tmp.value
                        current = tmp
                        continue
                    return
                elif value < current.value:
                    if current.left is None:
                        return
                    else:
                        parent = current
                        current = current.left
                else:
                    if current.right is None:
                        return
                    else:
                        parent = current
                        current = current.right

    def exist(self, value, count_visited=False):
        """ Check if a value exist in the tree and count the number of visited nodes
            :param value: the value to check
            :param count_visited: if True, count the number of visited nodes
            :return: True if the value exist, False otherwise
        """
        self.visited = 0
        if self.root is None:
            return False
        else:
            current = self.root
            while True:
                if count_visited:
                    self.visited += 1
                if value == current.value:
                    return True
                elif value < current.value:
                    if current.left is None:
                        return False
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        return False
                    else:
                        current = current.right

    def is_empty(self):
        """ Check if the tree is empty
            :return: True if the tree is empty, False otherwise
        """
        if self.root is None:
            return True

    def clear(self):
        """ Clear the tree
        """
        self.root = None

    def union(self, other):
        """ Create a new tree that is the union of self and other
            :param other: the other tree
            :return: the new tree
        """
        new_tree = ABR()
        if self.root is not None:
            self._union(self.root, new_tree)
        if other.root is not None:
            self._union(other.root, new_tree)
        return new_tree

    def _union(self, node, new_tree):
        """ Recursive function to create a new tree that is the union of self and other
            :param node: the current node
            :param new_tree: the new tree
        """
        new_tree.insert(node.value)
        if node.left is not None:
            self._union(node.left, new_tree)
        if node.right is not None:
            self._union(node.right, new_tree)

    def intersection(self, other):
        """ Create a new tree that is the intersection of self and other
            :param other: the other tree
            :return: the new tree
        """
        new_tree = ABR()
        if self.root is not None:
            self._intersection(self.root, other, new_tree)
        return new_tree

    def _intersection(self, node, other, new_tree):
        """ Recursive function to create a new tree that is the intersection of self and other
            :param node: the current node
            :param other: the other tree
            :param new_tree: the new tree
        """
        if other.exist(node.value):
            new_tree.insert(node.value)
        if node.left is not None:
            self._intersection(node.left, other, new_tree)
        if node.right is not None:
            self._intersection(node.right, other, new_tree)

    def display_infixe(self):
        """ Display the tree in infixe order
        """
        if self.root is not None:
            self._display_infixe(self.root)
            print()

    def _display_infixe(self, root):
        """ Recursive function to display the tree in infixe order
            :param root: the current node
        """
        if root.left is not None:
            self._display_infixe(root.left)
        print(root.value, end=' ')
        if root.right is not None:
            self._display_infixe(root.right)

    def display_prefixe(self):
        """ Display the tree in prefixe order
        """
        if self.root is not None:
            self._display_prefixe(self.root)
            print()

    def _display_prefixe(self, root):
        """ Recursive function to display the tree in prefixe order
            :param root: the current node
        """
        print(root.value, end=' ')
        if root.left is not None:
            self._display_prefixe(root.left)
        if root.right is not None:
            self._display_prefixe(root.right)

    def display_bfs(self):
        """ Display the tree in breadth first search order
        """
        if self.root is not None:
            queue = [self.root]
            while len(queue) > 0:
                node = queue.pop(0)
                print(node.value, end=' ')
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            print()

    def height_tree(self):
        """ Calculate the height of the tree
            :return: the height of the tree
        """
        if self.root is None:
            return 0
        else:
            return self._height_tree(self.root)

    def _height_tree(self, node):
        """ Recursive function to calculate the height of the tree
            :param node: the current node
            :return: the height of the tree
        """
        if node.left is None and node.right is None:
            return 0
        elif node.left is None:
            return 1 + self._height_tree(node.right)
        elif node.right is None:
            return 1 + self._height_tree(node.left)
        else:
            return 1 + max(self._height_tree(node.left), self._height_tree(node.right))


class TestNode(unittest.TestCase):

    def test_node_creation(self):
        # Test node creation and attribute initialization
        node = Node(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_left_and_right_children(self):
        # Test setting and getting left and right children
        node = Node(5)
        left_child = Node(3)
        right_child = Node(7)
        node.left = left_child
        node.right = right_child
        self.assertEqual(node.left, left_child)
        self.assertEqual(node.right, right_child)

    def test_node_value(self):
        # Test changing the node value
        node = Node(5)
        node.value = 10
        self.assertEqual(node.value, 10)


class TestABR(unittest.TestCase):
    def setUp(self):
        self.tree = ABR()

    def test_insert(self):
        self.tree.insert(5)
        self.assertEqual(self.tree.root.value, 5)
        self.tree.insert(3)
        self.assertEqual(self.tree.root.left.value, 3)

    def test_is_empty(self):
        self.assertTrue(self.tree.is_empty())
        self.tree.insert(5)
        self.assertFalse(self.tree.is_empty())

    def test_clear(self):
        self.tree.insert(5)
        self.tree.clear()
        self.assertIsNone(self.tree.root)

    def test_exist(self):
        self.tree.insert(5)
        self.assertTrue(self.tree.exist(5))
        self.assertFalse(self.tree.exist(3))
        self.tree.insert(3)
        self.assertTrue(self.tree.exist(3))

    def test_delete(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.delete(5)
        self.assertFalse(self.tree.exist(5))
        self.assertTrue(self.tree.exist(3))
        self.assertTrue(self.tree.exist(7))
        self.tree.delete(3)
        self.assertFalse(self.tree.exist(3))

    def test_height_tree(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.assertEqual(self.tree.height_tree(), 1)

    def test_union(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        other = ABR()
        other.insert(5)
        other.insert(3)
        other.insert(9)
        new_tree = self.tree.union(other)
        self.assertTrue(new_tree.exist(5))
        self.assertTrue(new_tree.exist(3))
        self.assertTrue(new_tree.exist(7))
        self.assertTrue(new_tree.exist(9))
        self.assertEqual(new_tree.height_tree(), 2)

    def test_intersection(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        other = ABR()
        other.insert(5)
        other.insert(3)
        other.insert(9)
        new_tree = self.tree.intersection(other)
        self.assertTrue(new_tree.exist(5))
        self.assertTrue(new_tree.exist(3))
        self.assertFalse(new_tree.exist(7))
        self.assertFalse(new_tree.exist(9))
        self.assertEqual(new_tree.height_tree(), 1)

    def test_display_infixe(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        with Capturing() as output:
            self.tree.display_infixe()
        self.assertEqual(['3', '5', '7'], output.pop(0).split())
        self.tree.insert(4)
        with Capturing() as output:
            self.tree.display_infixe()
        self.assertEqual(['3', '4', '5', '7'], output.pop(0).split())
        self.tree.insert(4)
        with Capturing() as output:
            self.tree.display_infixe()
        self.assertEqual(['3', '4', '5', '7'], output.pop(0).split())

    def test_display_prefixe(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        with Capturing() as output:
            self.tree.display_prefixe()
        self.assertEqual(['5', '3', '7'], output.pop(0).split())
        self.tree.insert(4)
        with Capturing() as output:
            self.tree.display_prefixe()
        self.assertEqual(['5', '3', '4', '7'], output.pop(0).split())
        self.tree.insert(4)
        with Capturing() as output:
            self.tree.display_prefixe()
        self.assertEqual(['5', '3', '4', '7'], output.pop(0).split())

    def test_display_bfs(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        with Capturing() as output:
            self.tree.display_bfs()
        self.assertEqual(['5', '3', '7'], output.pop(0).split())
        self.tree.insert(4)
        with Capturing() as output:
            self.tree.display_bfs()
        self.assertEqual(['5', '3', '7', '4'], output.pop(0).split())
        self.tree.insert(4)
        with Capturing() as output:
            self.tree.display_bfs()
        self.assertEqual(['5', '3', '7', '4'], output.pop(0).split())


class TestPerf(unittest.TestCase):

    # Method to test the performance of the ABR
    def test_perf(self):
        print("--------- Performance  ---------")
        # Create a tree
        tree = ABR()
        # Insert 5000 random values between 0 and 10000, measure the time, and measure the height of the tree
        start = time.time()
        for i in range(5000):
            tree.insert(random.randint(0, 10000))
        end = time.time()
        height = tree.height_tree()
        # Print the results
        print("--------- Insertion.png  -----------")
        print("Time to insert 5000 values in the tree: {}s".format(end - start))
        print("Height of the tree: {}".format(height))
        print("-------------------------------")
        # Search.png for 100 random values between 0 and 10000, measure the time
        start = time.time()
        visited = {}
        for i in range(100):
            tree.exist(random.randint(0, 10000), True)
            visited[i] = tree.get_visited()
        end = time.time()
        # Print the results
        print("--------- Search.png  -----------")
        print("Time to search 100 values in the tree: {}s".format(end - start))
        print("Average visited nodes: {}".format(sum(visited.values()) / len(visited)))
        print("-------------------------------")
        print()

    # method to test the performance of the ABR on different height
    def test_perf_on_different_height(self):
        print("--------- Performance  ---------")
        # compute the average time for 1000 iterations with differents height
        ten_height = ABR()
        hundred_height = ABR()
        thousand_height = ABR()
        ten_thousand_height = ABR()
        million_height = ABR()
        # Insert values in the tree to obtain height of 10, 100, 1000, 10000, 100000
        while ten_height.height_tree() < 10:
            ten_height.insert(random.randint(0, 1000000000000000))
        while hundred_height.height_tree() < 100:
            hundred_height.insert(random.randint(0, 1000000000000000))
        while thousand_height.height_tree() < 1000:
            thousand_height.insert(random.randint(0, 1000000000000000))
        while ten_thousand_height.height_tree() < 10000:
            ten_thousand_height.insert(random.randint(0, 1000000000000000))
        while million_height.height_tree() < 100000:
            million_height.insert(random.randint(0, 1000000000000000))

        # Search.png for 100 values in each tree, measure the time, and do a graph in fact of the time and the height
        times = {
            10: 0,
            100: 0,
            1000: 0,
            10000: 0,
            100000: 0
        }
        for i in range(100):
            t1 = time.time()
            ten_height.exist(random.randint(0, 1000000000000000))
            t2 = time.time()
            times[10] += t2 - t1
            t1 = time.time()
            hundred_height.exist(random.randint(0, 1000000000000000))
            t2 = time.time()
            times[100] += t2 - t1
            t1 = time.time()
            thousand_height.exist(random.randint(0, 1000000000000000))
            t2 = time.time()
            times[1000] += t2 - t1
            t1 = time.time()
            ten_thousand_height.exist(random.randint(0, 1000000000000000))
            t2 = time.time()
            times[10000] += t2 - t1
            t1 = time.time()
            million_height.exist(random.randint(0, 1000000000000000))
            t2 = time.time()
            times[100000] += t2 - t1
        # Print the results
        print("--------- Search.png  -----------")
        print("Average time to search 100 values in the tree with height of 10: {}s".format(times[10] / 100))
        print("Average time to search 100 values in the tree with height of 100: {}s".format(times[100] / 100))
        print("Average time to search 100 values in the tree with height of 1000: {}s".format(times[1000] / 100))
        print("Average time to search 100 values in the tree with height of 10000: {}s".format(times[10000] / 100))
        print("Average time to search 100 values in the tree with height of 100000: {}s".format(times[100000] / 100))
        print("-------------------------------")
        print()
        # Plot the graph
        plt.plot(times.keys(), times.values())
        plt.xlabel('Height')
        plt.ylabel('Time')
        plt.title('Time in function of the height')
        plt.show()






if __name__ == '__main__':
    unittest.main()
