# 'annotations' enables class typing within its own class
from __future__ import annotations

# advanced typing - Optional[Type] = Type | None, Iterable = iterator protocol implemented
from typing import Optional, Iterable



class Element():
    def __init__(self, value=None, previous_elem: Optional[Element] = None, next_elem: Optional[Element] = None):
        """
        This is the constructor for an Element object, which is a single node in the linked list.
        It initializes the value of the element, its previous and next elements in the list.
        It takes three optional arguments:
        :param value: the value of the element
        :param previous_elem: the previous element in the list
        :param next_elem: the next element in the list
        """
        self._value = value
        self._previous = previous_elem
        self._next = next_elem

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, value):
        self._previous = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value



class LinkedList():

    def __init__(self, val_iter: Optional[Iterable] = []):
        """
        This is the constructor for a LinkedList object,
        which initializes the first and last elements of the list,
        the current element, and the length of the list.
        It takes an optional iterable argument to populate the list or with an empty list
        :param val_iter:
        """
        # the first and the end item in the list
        self._first: Optional[Element] = None
        self._end: Optional[Element] = None
        self._current_elem: Optional[Element] = None
        self._len = 0

        if val_iter:
            for value in val_iter:
                self.append(value)

        self._current_elem = self._first

    def __str__(self):
        str_text = "["
        count = 0
        for link in self:
            if count == 0:
                str_text += f"{link},"
            elif count == self._len - 1:
                str_text += f" {link}]"
            else:
                str_text += f" {link},"
            count += 1
        return str_text

    def __iter__(self):
        self._current_elem = self._first
        return self

    def __next__(self):
        if not self._current_elem:
            self._current_elem = self._first
            raise StopIteration()
        current_return = self._current_elem
        self._current_elem = self._current_elem.next
        return current_return.value

    def __len__(self):
        return self._len

    def __getitem__(self, item):
        self._current_elem = self._first
        # If the user enters a number that is greater than the length of the list.
        if item+1 > self._len:
            raise IndexError('list index out of range')

        for inx in range(item):
            self._current_elem = self._current_elem.next
        return self._current_elem.value

    def __add__(self, other: LinkedList) -> LinkedList:
        if not isinstance(other, LinkedList):
            raise Exception()
        new_list = LinkedList()
        for item in self:
            new_list.append(item)

        for item in other:
            new_list.append(item)

        return new_list

    def append(self, value):
        """
        This method adds a new element to the end of the linked list.
        """
        elem_val = Element(value=value)
        if not self._first:
            self._first = elem_val

        else:
            self._current_elem = self._end
            self._current_elem.next = elem_val
            prev = self._current_elem
            self._current_elem = elem_val
            self._current_elem.previous = prev
        self._end = elem_val
        self._len += 1

    def insert_at(self, value, index: int = None):
        """
        This method inserts a new element at the given index in the linked list.
        If the index is None or greater than the length of the list,
        the new element will be added to the end of the list.
        :param value:
        :param index:
        :return:
        """
        if index is None or index > self._len - 1:
            self.append(value)
        else:
            elem_val = Element(value)
            self._current_elem = self._first
            for inx in range(index):
                self._current_elem = self._current_elem.next

            elem_val.next = self._current_elem
            elem_val.previous = self._current_elem.previous
            prev = self._current_elem.previous
            self._current_elem.previous = elem_val
            prev.next = elem_val
            self._len += 1

    def remove_from(self, index: int):
        """
        This method removes an element from the given index in the linked list.
        """
        if index > self._len - 1:
            raise IndexError('list index out of range')

        for inx in range(index):
            self._current_elem = self._current_elem.next

        prev = self._current_elem.previous
        nex = self._current_elem.next
        prev.next = nex
        nex.previous = prev
        self._len -= 1










