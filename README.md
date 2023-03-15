# linkedList
This is a Python implementation of a linked list data structure. A linked list is a data structure consisting of a sequence of elements, each pointing to the next element in the sequence. It is a dynamic data structure, meaning that it can grow or shrink in size during runtime.

## Getting Started
To use this implementation of a linked list, you can simply import the LinkedList class from the linked_list.py file.

```python
from linked_list import LinkedList
```

## Usage

### Creating a linked list
To create an empty linked list, simply instantiate a new **LinkedList** object.

```python
my_list = LinkedList()
```

You can also initialize a linked list with a list of values by passing an iterable as an argument.

```python
my_list = LinkedList([1, 2, 3, 4])
```

###### Appending an element
To add an element to the end of a linked list, use the **append** method.

```python
my_list.append(5)
```

###### Inserting an element
To insert an element at a specific index in the linked list, use the **insert_at** method.

```python
my_list.insert_at(6, 2)
```

If the index is not specified or is greater than the length of the list, the element will be added to the end of the list.

```python
my_list.insert_at(7)
```

###### Removing an element
To remove an element at a specific index in the linked list, use the **remove_from** method.

```python
my_list.remove_from(3)
```

###### Iterating over the list
To iterate over the linked list, use the **for** loop.

```python
for value in my_list:
    print(value)
    ```
    
You can also use the **__getitem__** method to access elements by index.

```python
value = my_list[2]
```

###### Concatenating two linked lists
To concatenate two linked lists, use the **+** operator.

```python
my_other_list = LinkedList([8, 9, 10])
new_list = my_list + my_other_list
```

###### Getting the length of the list
To get the length of the linked list, use the **len** function.

```python
length = len(my_list)
```

## Running the tests
To run the unit tests for this implementation of a linked list, run the following command:

```terminal
python test_linked_list.py
```
