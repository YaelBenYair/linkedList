import unittest
from typing import List
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_append(self):
        # Test that append method works correctly
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual(len(llist), 3)
        self.assertEqual(llist[0], 1)
        self.assertEqual(llist[1], 2)
        self.assertEqual(llist[2], 3)

    def test_insert_at(self):
        # Test that insert_at method works correctly
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(4)
        llist.insert_at(3, 2)
        self.assertEqual(len(llist), 4)
        self.assertEqual(llist[0], 1)
        self.assertEqual(llist[1], 2)
        self.assertEqual(llist[2], 3)
        self.assertEqual(llist[3], 4)

    def test_insert_at_end(self):
        # Test that insert_at method adds element at the end if index is None
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.insert_at(3)
        self.assertEqual(len(llist), 3)
        self.assertEqual(llist[0], 1)
        self.assertEqual(llist[1], 2)
        self.assertEqual(llist[2], 3)

    def test_insert_at_big_index(self):
        # Test that insert_at method adds element at the end if index is greater than length of list
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.insert_at(3, 100)
        self.assertEqual(len(llist), 3)
        self.assertEqual(llist[0], 1)
        self.assertEqual(llist[1], 2)
        self.assertEqual(llist[2], 3)

    def test_remove_from(self):
        # Test that remove_from method works correctly
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.remove_from(1)
        self.assertEqual(len(llist), 3)
        self.assertEqual(llist[0], 1)
        self.assertEqual(llist[1], 3)
        self.assertEqual(llist[2], 4)

    def test_remove_from_zero(self):
        # Test that remove_from method removes first element correctly
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.remove_from(0)
        self.assertEqual(len(llist), 3)
        self.assertEqual(llist[0], 2)
        self.assertEqual(llist[1], 3)
        self.assertEqual(llist[2], 4)

    def test_remove_from_end(self):
        # Test that remove_from method removes last element correctly
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.remove_from(3)
        self.assertEqual(len(llist), 3)
        self.assertEqual(llist[0], 1)
        self.assertEqual(llist[1], 2)
        self.assertEqual(llist[2], 3)

    def test_add(self):
        # Test that add operator works correctly
        linked_list_1 = LinkedList([1, 2, 3])
        linked_list_2 = LinkedList([4, 5, 6])
        new_linked_list = linked_list_1 + linked_list_2
        self.assertEqual(str(new_linked_list), "[1, 2, 3, 4, 5, 6]")

    def test_len(self):
        linked_list = LinkedList([1, 2, 3])
        self.assertEqual(len(linked_list), 3)

    def test_getitem(self):
        linked_list = LinkedList([1, 2, 3])
        self.assertEqual(linked_list[0], 1)
        self.assertEqual(linked_list[1], 2)
        self.assertRaises(Exception, linked_list.__getitem__, 3)

    def test_append2(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(str(linked_list), '[1, 2, 3]')

    def test_len2(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(len(linked_list), 5)
        linked_list.append(6)
        self.assertEqual(len(linked_list), 6)

    def test_getitem2(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(linked_list[0], 1)
        self.assertEqual(linked_list[2], 3)
        with self.assertRaises(Exception):
            linked_list[5]

    def test_insert_at2(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])
        linked_list.insert_at(0, 0)
        self.assertEqual(str(linked_list), '[0, 1, 2, 3, 4, 5]')
        linked_list.insert_at(6, 6)
        self.assertEqual(str(linked_list), '[0, 1, 2, 3, 4, 5, 6]')
        linked_list.insert_at(99, 3)
        self.assertEqual(str(linked_list), '[0, 1, 2, 99, 3, 4, 5, 6]')

    def test_remove_from2(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])
        linked_list.remove_from(0)
        self.assertEqual(str(linked_list), '[2, 3, 4, 5]')
        linked_list.remove_from(3)
        self.assertEqual(str(linked_list), '[2, 3, 4]')
        with self.assertRaises(Exception):
            linked_list.remove_from(3)

    def test_add2(self):
        linked_list1 = LinkedList([1, 2, 3])
        linked_list2 = LinkedList([4, 5, 6])
        linked_list3 = linked_list1 + linked_list2
        self.assertEqual(str(linked_list3), '[1, 2, 3, 4, 5, 6]')
        with self.assertRaises(Exception):
            linked_list1 + [7, 8, 9]

    def test_iter_empty_list(self):
        # Test iterating over an empty list
        linked_list = LinkedList()
        result = []
        for elem in linked_list:
            result.append(elem)
        self.assertEqual(result, [])

    def test_iter_nonempty_list(self):
        # Test iterating over a non-empty list
        linked_list = LinkedList([1, 2, 3])
        result = []
        for elem in linked_list:
            result.append(elem)
        self.assertEqual(result, [1, 2, 3])

    def test_iter_modify_list(self):
        # Test iterating over a list and modifying it
        linked_list = LinkedList([1, 2, 3])
        result = []
        for elem in linked_list:
            result.append(elem)

        for elem in result:
            linked_list.append(elem * 2)
        self.assertEqual(result, [1, 2, 3])
        self.assertEqual(str(linked_list), "[1, 2, 3, 2, 4, 6]")


if __name__ == '__main__':
    unittest.main()







