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
