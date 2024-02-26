# Python Interview Cheatsheet

## Python collections

- **List** is a collection which is `ordered and changeable`. Allows duplicate members.
  - Can have all type of data types
  - Can use Sort function but gives error for different data types.
- **Tuple** is a collection which is `ordered and unchangeable`. Allows duplicate members.
  - Can have all type of data types
- **Set** is a collection which is `unordered, unchangeable\*, and unindexed`. No duplicate members.
  - Elements in `Set` needs to be `hashable`
  - As per definition, a set can have any number and any items. However, mutable elements such as dictionaries, lists, or sets are not allowed as its elements.
- **Dictionary** is a collection which is `ordered\*\* and changeable`. No duplicate 
members.
  - Key of `dict` needs to be `hashable`
  -  The Key is normally a string, but can be any hashable type

```
  \*Set items are unchangeable, but you can remove items and add new items.
  \*\*As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
```

## List of Mutable and Immutable objects

### Objects of built-in type that are mutable are:

- Lists
- Sets
- Dictionaries
- User-Defined Classes (It purely depends upon the user to define the characteristics)

### Objects of built-in type that are immutable are:

- Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
- Strings
- Tuples
- Frozen Sets
- User-Defined Classes (It purely depends upon the user to define the characteristics)

``` All immutable object (string, number, boolean, Tuples) are hashable but opposite is not True```
## Basic Knowledge, Good practices

- **PEP 8** sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code.
- **REST** - Representational state transfer
- **NaN** - Not A Number
- A **package** is a collection of Python modules: while a **module** is a single Python file, a package is a directory of Python modules containing an additional **init**.py file, to distinguish a package from a directory that just happens to contain a bunch of Python scripts.
- Statelessness means that every HTTP request happens in complete isolation. When the client makes an HTTP request, it includes all information necessary for the server to fulfill the request.
  The server never relies on information from previous requests from the client. If any such information is important then the client will send that as part of the current request.

## Some important concepts

- https://www.codesansar.com/python-programming/what-is-pickling-and-unpickling.htm

## In Python, tuples and lists are both used to store collections of items, but they have some key differences in terms of mutability and storage in memory.

### Lists:
- Lists are mutable, meaning you can modify their elements (add, remove, or modify items).
- Lists are implemented as dynamic arrays, which means they allocate more memory than they currently need to accommodate potential future growth.
- Because of their dynamic nature, lists may result in more memory overhead compared to tuples.

### Tuples:
- Tuples are immutable, meaning their elements cannot be modified after creation. Once a tuple is created, you cannot add, remove, or change its elements.
- Tuples are implemented as fixed-size arrays. This means they allocate exactly the amount of memory required for the elements they contain.
- Due to their fixed-size nature, tuples generally have less memory overhead compared to lists.

### Memory Storage:
- Both lists and tuples store references to the objects they contain, not the actual objects themselves. This is true for elements of any type, whether they are integers, strings, or other objects.
- Each element in a list or tuple is stored in a contiguous block of memory.
- The difference lies in the mutability and size flexibility. Lists, being mutable and dynamically sized, may need to allocate more memory than their current usage to allow for growth. Tuples, being immutable and fixed-size, allocate memory exactly as needed.

Here is a simplified illustration:

```python
# Example of memory representation (simplified)

# List
my_list = [1, 2, 3]
# Memory representation: |ref1|ref2|ref3|

# Tuple
my_tuple = (1, 2, 3)
# Memory representation: |ref1|ref2|ref3|
```

In both cases, the references (ref1, ref2, ref3) point to the actual objects (1, 2, 3) in memory. The primary difference lies in the mutability and memory allocation strategy of lists versus the immutability and fixed-size nature of tuples.

## Both sets and dictionaries in Python use a hash table to store their elements, but they have different purposes and structures.

### Sets:
- A set is an unordered collection of unique elements.
- Sets use a hash table to achieve fast average-case time complexity for basic operations like add, remove, and membership test.
- The elements of a set are hashed, and the hash values are used to determine the position of elements in the hash table.
- Since sets are unordered, the order in which elements were inserted is not guaranteed to be maintained.

### Dictionaries (dict):
- A dictionary is a collection of key-value pairs, where each key must be unique.
- Dictionaries also use a hash table to provide efficient key-based lookups, insertions, and deletions.
- Keys are hashed, and the hash values are used to determine the position of key-value pairs in the hash table.
- The combination of key and value makes up an entry in the dictionary.

Here's a simplified explanation of the storage mechanism:

```python
# Example set in memory (simplified)
my_set = {1, 2, 3}

# Memory representation:
# | Hash(1) | Hash(2) | Hash(3) |

# Example dictionary in memory (simplified)
my_dict = {'a': 10, 'b': 20, 'c': 30}

# Memory representation:
# | Hash('a') | Hash('b') | Hash('c') |
# |   10      |    20     |    30     |
```

In both cases, the hash values determine the position of elements or key-value pairs in the hash table. This hashing mechanism allows for efficient retrieval and modification of elements or values. The use of hash tables provides average-case constant time complexity for basic operations, assuming a good hash function and proper handling of collisions.
