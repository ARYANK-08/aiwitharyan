

# Python Programming Overview

Python is a versatile programming language that supports both Object-Oriented Programming (OOP) and Functional Programming.

**Python is driving the latest advancements in AI, including:**
- **Text to Images**
- **Large Language Models (LLMs)**
- **Deep Learning**

**Used by leading companies:**
- **Tesla**: Utilizes OpenCV
- **Instagram**: Employs Django

## Use Cases
- **AI & ML**
- **Computer Vision**
- **Web Applications** (e.g., Flask, Django)
- **Data Analytics and Visualization**

## Variables
Variables in Python act as containers for storing data values.

### Data Types
- **Integer**: `a = 1`
- **Boolean**: `b = False`
- **String**: `c = "Aryan"`
- **NoneType**: `d = None`

### Number Data Types
1. **Number**: Integer, Float, Complex
   - `int`: `3`, `-8`, `0`
   - `float`: `3.8`, `0.001`, `-9.0`
   - **complex**: `2 + 3j`, syntax: `a = complex(123, 2)` -> `123 + 2j`

2. **Text Data**: `str`
   - Example: `"Hello God Level Engineer"`

3. **Boolean Data**: `True` or `False`

4. **Sequenced Data**: `list`, `tuple`
   - **List**: An ordered collection of data with elements separated by commas and enclosed within square brackets.
     - Lists are mutable and can be modified.
     - Example: `list1 = [B, 2.3, [-4, 5], ['apple']]`
   
   - **Tuple**: *Immutable* ordered collection of data within elements separated by commas and enclosed within parentheses.
     - Tuples are immutable and cannot be modified.
     - Example: `tuple1 = (("aryan", "myron"), ("pradyumnaa", "sharvin"))`

   - **Mutable vs Immutable**:
     - Mutation refers to changes (e.g., the tail of a human vanishing).

   > **Note**: Lists are mutable, and tuples are immutable.

5. **Mapped Data**: `dictionary` (or `dict`)
   - A collection of key-value pairs.
   - Example: `dict1 = { "name": "aryan", "age": 20, "girlfriends": 0, "canCode": True }`

   > **Note**: In Python, everything is an OBJECT! This includes dictionaries, integers, and booleans.

## Operators
| Operator | Operator Name      | Example |
|----------|---------------------|---------|
| +        | Addition            | `5 + 7` |
| -        | Subtraction         | `5 - 7` |
| *        | Multiplication      | `5 * 7` |
| /        | Division            | `5 / 7` |
| %        | Modulus             | `5 % 7` |
| //       | Floor Division      | `5 // 7` |
| **       | Exponentiation      | `5 ** 2` |

## Type Casting
Type casting refers to converting one data type into another. In Python, this is known as type conversion.

### Functions
- `int()`, `float()`, `str()`, `ord()`, `hex()`, `oct()`, `tuple()`, `list()`, `set()`, `dict()`

### Types of Type Casting
- **Explicit Conversion**: Done manually by the developer.
- **Implicit Conversion**: Automatically performed by Python.

```python
a = "1"  # string
b = "2"
print(int(a) + int(b))  # string to number
```

```python
c = 1.9  # float
d = 8     # int
# d is converted into float because it's a higher order data type
print(c + d)
```

## Taking User Input
Use the `input()` function, which returns a value as a string.

```python
x = input("Enter first number: ")
y = input("Enter second number: ")
print(x + y)
```

**Output**: `12100` (because strings are concatenated)

To perform addition, you need to type cast to integer format:

```python
print(int(x) + int(y))  # type casting
```

## String Handling

**Strings** are sequences of textual data enclosed within single or double quotation marks.

### Accessing Characters
- Example: `name = "aryan"`
  
  ```python
  print(name[0])  # Output: 'a'
  print(name[1])  # Output: 'r'
  ```

Strings can be accessed like arrays with indices starting from 0.

### String Slicing
Slicing refers to extracting parts of a string using indices.

```python
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word")
```

**String as an Array**:
- Strings are sequences of characters.

```python
pie = "Apple Pie"
print(pie[:5])  # Output: 'Apple'
print(pie[6])   # Output: 'i'
```
```python
conditions = [
(3, "fizz"),
(5, "buzz"),
(7, "bizz"),
(9, "bazz")]

for i in range(1, 100):
    output = "".join(word for divisor, word in conditions if i % divisor == 0)
    if not output:
        output = str(i)
    print(output, i)
```
### String Methods
- **`upper()`**: Converts the string to uppercase.
  
  ```python
  str = "AbcdEfghIJ"
  print(str.upper())  # Output: 'ABCDEFGHIJ'
  ```

- **`lower()`**: Converts the string to lowercase.

- **`strip()`**: Removes whitespace before and after the string.

  ```python
  str = "Silver   Spoon  "
  print(str.strip())  # Output: 'Silver   Spoon'
  ```

- **`rstrip()`**: Removes trailing characters.

  ```python
  str = "hello!!!"
  print(str.rstrip("!"))  # Output: 'hello'
  ```

- **`replace()`**: Replaces all occurrences of a string with another string.

  ```python
  str = "Silver spoon"
  print(str.replace("Sp", "M"))  # Output: 'Milver moon'
  ```

- **`split()`**: Splits the string at specified instances and returns a list.

  ```python
  str2 = "Silver spoon"
  print(str2.split(" "))  # Output: ['Silver', 'spoon']
  ```

- **`capitalize()`**: Capitalizes the first character of the string.

- **`center()`**: Aligns the string to the center.

- **`count()`**: Returns the number of occurrences of a value within the string.

  ```python
  str = "abracadabra"
  countStr = str.count("a")
  print(countStr)  # Output: 5
  ```

- **`endswith()`**: Checks if the string ends with a given value.

- **`find()`**: Searches for the first occurrence of a value and returns its index. Returns `-1` if not found.

  ```python
  str = "He's name is aryan and he is good"
  print(str.find("is"))  # Output: 6
  print(str.find("Daniel"))  # Output: -1
  ```

  > **Note**: `index()` raises an exception if the value is absent, while `find()` returns `-1`.

- **`isalnum()`**: Returns `True` if the string contains only alphanumeric characters (A-Z, a-z, 0-9).

- **`islower()`**: Returns `True` if all characters in the string are lowercase.

- **`isprintable()`**: Returns `True` if all characters in the string are printable.

- **`isspace()`**: Returns `True` if the string consists of whitespace characters.

- **`istitle()`**: Returns `True` if the string is in title case (each word's first letter is capitalized).

- **`isupper()`**: Returns `True` if all characters in the string are uppercase.

## Conditional Statements
- **`if`**: Basic conditional.
- **`if-else`**: Conditional with alternative execution.
- **`if-else-elif`**: Multiple conditions.
- **Nested `if-else-elif`**: Conditions within conditions.

### Example
```python
iphonePrice = 60000
budget = 20000
if budget < iphonePrice:
    print("Kamao bsdk!")
else:
    print("lele bhai")
```

### `elif` Statements
```python
num = 0
if num < 0:
    print("number is negative")
elif num == 0:
    print("number is zero")
else:
    print("number is positive")
```

### Nested `if`
```python
num = 18
if num < 0:
    print("Number is negative")
elif num > 0:
    if num <= 10:
        print("number is between 1-10")
    elif num > 10 and num <= 20:
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")
```
**Output**: `number is between 11-20`

### Conditional Operators
Conditional operators are used to compare values. Here are some examples:

- **Operators**: `>`, `<`, `>=`, `<=`, `==`
  
  ```python
  a = 18
  print(a > 18)   # Output: False
  print(a <= 18)  # Output: True
  print(a == 18)  # Output: True
  print(a != 18)  # Output: False
  ```

## For Loops
A `for` loop in Python iterates over a sequence of iterable objects, such as strings, lists, tuples, sets, and dictionaries.

- **Example with Strings**:
  ```python
  name = "Martin"
  for i in name:
      print(i, end=", ")
  # Output: M, a, r, t, i, n
  ```

- **Example with Lists**:
  ```python
  colors = ["red", "green", "blue"]
  for i in colors:
      print(i)
      for b in i:
          print(b)
  ```

- **Example with Range**:
  ```python
  for k in range(1, 200):
      print(k)  # Output: Numbers from 1 to 199
  ```

  ```python
  for k in range(2, 12, 2):
      print(k)  # Output: 2, 4, 6, 8, 10
  ```

## While Loop
A `while` loop repeatedly executes a block of code as long as a condition is `True`.

```python
count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("I am inside else")
```

### Do-While Loop
Python does not have a built-in `do-while` loop, but you can simulate it using a `while` loop.

```python
# This is a pseudo code representation as Python does not support do-while syntax
do:
{
    # loop body
}
while (condition)
```

## Break & Continue
- **`break`**: Exits the loop immediately.
- **`continue`**: Skips the rest of the code inside the current iteration of the loop.

- **Example with `break`**:
  ```python
  for i in range(1, 101):
      print(i, end=" ")
      if i == 50:
          break
      else:
          print("aryan")
  # Output: 1 aryan 2 aryan ... 48 aryan 49 aryan 50
  ```

- **Example with `continue`**:
  ```python
  for i in range(12):
      if i == 10:
          print("Skip the iteration")
          continue
      print("5 x", i, "=", 5 * i)
  # Output: 5 x 0 = 0 ... 5 x 9 = 45 Skip the iteration 5 x 11 = 55
  ```

## Python Functions
A function is a block of code that performs a specific task whenever it is called. Functions help make code neater and more reusable.

- **Built-in Functions**: `min()`, `max()`, `len()`, `sum()`, `type()`, `tuple()`, `list()`, `set()`, `print()`, `range()`, `dict()`
  
- **User-Defined Functions**: Functions created to perform specific tasks as per the needs of the user.

  **Example**:
  ```python
  def greet(fname, lname):
      print("Hello", fname, lname)

  greet("aryan", "kyatham")
  ```

## Function Arguments
- **Default Arguments**: Provide default values for function parameters.

  ```python
  def greet(fname, mname="ajay", lname="sharma"):
      print("Hello", fname, mname, lname)

  greet("disha")  # Output: Hello disha ajay sharma
  ```

- **Keyword Arguments**: Provide values in a key-value format, allowing you to skip the order of arguments.

  ```python
  def greet(fname, mname, lname):
      print("Hello", fname, mname, lname)

  greet(mname="Peter", lname="wesker", fname="Jaden")
  # Output: Hello Jaden Peter Wesker
  ```

- **Required Arguments**: All required arguments must be provided.

  ```python
  # This will raise an error because 'lname' is missing
  greet("aryan", "bhai")
  # Output: TypeError: greet() missing 1 required positional argument: 'lname'
  ```

- **Variable-Length Arguments**: Allow passing more arguments than defined.

  - **Arbitrary Arguments**:
    ```python
    def greet(*names):
        print("Hello", names[0], names[1], names[2])

    greet("aryan", "zayn", "khalid")
    ```

  - **Keyword Arguments**:
    ```python
    def greet(**names):
        print(names["fname"], names["mname"], names["lname"])

    greet(fname="Aryan", mname="Zayn", lname="Khalid")
    ```

- **Return Statement**: Returns the value of an expression back to the calling function.

  ```python
  def add(a, b):
      return a + b

  result = add(5, 3)
  print(result)  # Output: 8
  ```

## List
A list in Python is an ordered collection of data items. It allows you to store multiple items in a single variable. Lists are enclosed in square brackets (`[]`), with items separated by commas. Lists are mutable, meaning you can alter them after creation.

- **Examples**:
  ```python
  lst1 = [1, 2, 3, 4, 5, 6]
  lst2 = ["Red", "Green", "Blue"]
  details = ["Aryan", 20, "BTech"]
  ```

> **Check if an item is present in a list:**
> You can use the `in` keyword.
  ```python
  colors = ["Red", "Green", "Blue", "Yellow"]

  if "Yellow" in colors:
      print("Yellow is present")
  ```

### Range of Index
You can use indexing to access different parts of a list:

- **Print all elements from a given index to the end:**
  ```python
  animals = ["cat", "dog", "bat", "lion", "tiger", "goat", "cow"]
  print(animals[4:])
  ```

- **Print all elements from the start to a given index:**
  ```python
  print(animals[:6])
  ```

- **Print alternate values:**
  ```python
  print(animals[::2])
  ```

- **Print every 3rd element within a given range:**
  ```python
  print(animals[1:8:3])
  ```

## List Comprehension
List comprehensions are used to create new lists from other iterables like lists, tuples, dictionaries, sets, and even strings.

- **Example 1**: Accept items with the letter "o":
  ```python
  names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rose"]
  names_with_o = [item for item in names if "o" in item]
  print(names_with_o)
  # Output: ['Milo', 'Bruno', 'Rose']
  ```

- **Example 2**: Accept items with more than 4 letters:
  ```python
  names_with_4 = [item for item in names if len(item) > 4]
  ```

### List Methods
Here are some common methods to manipulate lists:

1. **`list.sort()`**: Sorts the list in ascending order.
   ```python
   colors = ["violet", "indigo", "blue", "green"]
   colors.sort()  # Output: ['blue', 'green', 'indigo', 'violet']
   ```

   **For descending order**:
   ```python
   nums = [4, 5, 1, 2, 3, 6, 7, 9, 8]
   nums.sort(reverse=True)
   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
   ```

2. **`list.reverse()`**: Reverses the list.
   ```python
   colors.reverse()
   ```

3. **`list.index()`**: Returns the index of the first occurrence of a specified item.
   ```python
   colors.index("green")
   ```

4. **`list.count()`**: Returns the count of items with a specified value.
   ```python
   colors.count("green")
   ```

5. **`list.copy()`**: Returns a shallow copy of the list.
   - Useful for performing operations on a copy without modifying the original list.
   ```python
   copy_colors = colors.copy()
   ```

6. **`list.append()`**: Appends an item to the end of the list.
   ```python
   colors = ["violet", "indigo"]
   colors.append("blue")
   # Output: ['violet', 'indigo', 'blue']
   ```

7. **`list.insert()`**: Inserts an item at a specified index.
   ```python
   colors = ["violet", "indigo"]
   colors.insert(1, "green")
   # Output: ['violet', 'green', 'indigo']
   ```

8. **`list.extend()`**: Adds elements from another list or collection to the end of the list.
   ```python
   colors = ["v", "i", "b"]
   rainbow = ["g", "y", "o", "r"]
   colors.extend(rainbow)
   # Output: ['v', 'i', 'b', 'g', 'y', 'o', 'r']
   ```

9. **Concatenating Two Lists**:
   ```python
   combined_list = color1 + color2
   ```

## Tuples :
- ordered collection of data items
- store multiple items in a single variable
- unchangeable - immutable : cant alter them

  ```
  tuple1 = (1, 2, 2, 3, 4, 5, 6)
  tuple2 = ("red", "green", "blue")
  details = ("abhijeet", 19, "Btech", 9.7)
  ```

  - Tuple Indexes :
       - each item/element in a tuple has its own unique index.
       - country = ("India", "Italy", "Spain")
       -             [0]       [1]       [2]
       - country[0] -> India

   - check for item in tuple using in keyword:
```python
country = ("India", "Italy", "Spain")
if "India" in country:
   print("india present")

```
Here's the beautified Markdown for your content:

### Manipulating Tuples

- Tuples are immutable, so if you want to add, remove, or change items in a tuple, you must first convert it to a **list**.
- **Tuple to List Conversion**:
  ```python
  countries = ["Italy", "India", "England"]
  temp = list(countries)
  temp.append("Germany")
  temp.pop(1)
  temp[2] = "Finland"
  countries = tuple(temp)
  print(countries)
  ```

> **Note**: You can concatenate two tuples directly without converting them to lists.
  ```python
  countries1 = ["India"]
  countries2 = ["England"]
  print(countries1 + countries2)
  ```

### Tuple Methods

1. **`count()`**: Returns the number of occurrences of a specified value.
   ```python
   tup1 = (1, 2, 3, 3, 3)
   print(tup1.count(3))  # Output: 3
   ```

2. **`index()`**: Returns the index of the first occurrence of a specified value.
   ```python
   tup1 = (1, 2, 3, 4)
   print(tup1.index(3))  # Output: 2
   ```

   > **Note**:
   > - `tup1 = (1)` creates an integer tuple, not a tuple. To create a single-item tuple, use `tup2 = (1,)`.
   >   ```python
   >   tup1 = (1)
   >   print(type(tup1))  # Output: <class 'int'>
   >   
   >   tup2 = (1,)
   >   print(type(tup2))  # Output: <class 'tuple'>
   ```

> **Note**: Tuples are used when the values should be constant and not changeable.

## F-Strings

F-Strings provide a way to embed expressions inside string literals, using curly braces `{}`.

```python
name = "Aryan"
print(f"Hey {name}")
```

### Python Docstrings

- Docstrings are string literals that appear right after the definition of a function, method, class, or module.
- They serve as documentation for the code.

```python
def square(n):
    '''Takes a number n and returns the square of n.'''
    print(n**2)

square(5)
```

## Python Comments vs. Docstrings

- **Comments**: Descriptions used to explain code to humans. They are ignored by the Python interpreter, similar to how your crush might ignore you!
- **Docstrings**: Documentation strings used immediately after the definition of a function, method, or class. They can be accessed using the `__doc__` attribute.

  ```python
  print(square.__doc__)
  ```

## PEP 8

- PEP 8 is a document that provides guidelines and best practices on how to write Python code.
- It aims to improve the readability and consistency of Python code.
- **PEP**: Python Enhancement Proposal
Here's the Markdown file for the provided content:


## Recursion : it is the process of defining something in terms of itself 
- We know that a function can call other functions, it's even possible for the function to call itself.

```python
def factorial(num):
   if (num == 1 or num == 0):
      return 1
   else:
      return (num * factorial(num-1))
```

#### Implementation:
```plaintext
5 x factorial(4)
5 x 4 x factorial(3)
5 x 4 x 3 x factorial(2)
5 x 4 x 3 x 2 x factorial(1)
factorial(1) returns 1
```

## Sets : unordered collection of data items
- They store multiple items in a single variable. Set items are separated by commas and enclosed within `{}`.
- Sets are unchangeable meaning you cannot change items of a set once created.
- Sets do not contain *DUPLICATE* items.

```python
info = {"aryan", 20, False, 5.9}
print(info) # order may change
```

- Here we see that items of a set occur in random order and hence they cannot be accessed using index numbers.
- Example: Check in the office which employees did not get a gift, take names of people without repeating names.

**Operations**: `add`, `union`, `difference`, `intersection`, `update`, `intersection_update`, `symmetric_difference`, `discard(no error)`, `remove(error)`

### Joining operations in sets:
1. `union()` and `update()`:
   - Prints all items present in two sets.
   - `update` adds items from another set into the existing set.

   ```python
   cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
   cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
   cities3 = cities1.union(cities2)
   print(cities3) # {'Tokyo', 'Madrid', 'Berlin', 'Delhi', 'Seoul', 'Kabul'}
   cities1.update(cities2)
   print(cities1) # {'Tokyo', 'Madrid', 'Berlin', 'Delhi', 'Seoul', 'Kabul'}
   ```

2. `intersection()` and `intersection_update()`:
   - Prints all items that are similar in both sets.

   ```python
   cities3 = cities1.intersection(cities2)
   print(cities3) # {"Madrid", "Tokyo"}
   cities1.intersection_update(cities2)
   print(cities1) # {"Madrid", "Tokyo"}
   ```

3. `symmetric_difference()` and `symmetric_difference_update()`:
   - Prints items in sets that are not similar.

   ```python
   print(cities1.symmetric_difference(cities2)) # {"Seoul", "Kabul", "Berlin", "Delhi"}
   ```

4. `difference()` and `difference_update()`:

**Set methods**:
1. `isdisjoint()`:
   - Checks if the items of a given set are present in another set.
   - Returns `True` if items are not present, `False` if items are present.

   ```python
   cities1.isdisjoint(cities2)
   ```

2. `issuperset()`:
   - Checks if all items of a particular set are present in the original set.
   - Returns `True` if items are present, `False` otherwise.

   ```python
   cities1.issuperset(cities2)
   ```

3. `issubset()`:
4. `add()`: 

   ```python
   cities1.add("Helsinki")
   ```

5. `update()`:

   ```python
   cities1.update(cities2)
   ```

6. `remove()/discard()`:
   - `remove`: 

     ```python
     cities1.remove("Tokyo") # raises error if "Tokyo" not found
     ```

   - `discard`:

     ```python
     cities2.discard("Tokyo") # no error if "Tokyo" not found
     ```

7. `pop()`: Random deletion.
8. `del`: Set delete.
9. `clear()`: 

## Python Dictionaries :
- Ordered collections of data items.
- Store multiple items in a single variable.
- Dictionaries are *Key-Value* pairs separated by commas and enclosed in `{}`.

```python
info = {"name": "aryan", "age": 19, "language": "python"}
```

1. Accessing single values:
   
   ```python
   info['name'] # 'aryan'
   info.get('language') # 'python'
   ```

2. Access multiple values and keys:
   
   ```python
   info.values() # dict_values(['aryan', 19, 'python'])
   info.keys() # dict_keys(['name', 'age', 'language'])
   ```

3. Access key-value pairs: `items()` method

   ```python
   for key, value in info.items():
       print(f"{key}: {value}")
   ```

**Dictionary methods**:
```python
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2) # {122: 45, 123: 89, 567: 69, 670: 69, 222: 67, 566: 90}
ep1.clear() # {}
ep1.pop(122) # removes key 122
ep1.popitem() # removes the last key-value pair
del ep1[122] # removes key 122
```

1. `update()`: Updates value of key provided if item already exists, else adds new key-value pair.

   ```python
   info = {'age': 19}
   info.update({'age': 20}) # 19 -> 20
   info.update({'DOB': 2003}) # adds 'DOB' in dict
   ```

2. `clear()`: Removes all items.
3. `pop(x)`: Removes key-pair value.
4. `popitem()`: Removes the last key-pair value.
5. `del`: Remove item or entire dict.

   > **Note**: `del` vs `pop`: `pop(x)` returns a value!

## For loop with else:
```python
for x in range(5):
   print(f"{x} number")
else:
   print("else block in loop")

x = 0
while x < 7:
   print(x)
   x += 1
else:
   print("sorry no x")
```
- `else` appears after the body of the loop.
- Executes after all iterations are completed in the loop.
- Program exits the loop only after the else block.

## Exception Handling:
```python
try:
   num = int(input("enter an integer"))
   a = [6, 3]
   print(a[num])
except IndexError:
   print("index error")
```

```python
a = input("enter the number")
print(f"Multiplication of {a} is:")
try:
   for i in range(1, 11):
       print(f"{int(a)} x {i} = {int(a) * i}")
except:
   print("invalid input")
```
- Process of responding to unwanted errors.
- Avoids program crashing.

## Finally clause: always executed (e.g., closing file, closing DB connection, ending program with a message)

**Using finally**:
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that handles the exception
    print("Cannot divide by zero.")
finally:
    # Code that will always be executed, regardless of exceptions
    print("This will always execute.")
```
In this example:

- If an exception occurs (like division by zero), the except block handles it.
- Regardless of whether an exception occurs or not, the finally block is executed. This ensures that clean-up code or important final steps are always performed.

**Without finally**:
If you don't use a finally block, you might have to rely on other mechanisms to ensure that certain code always runs, such as placing it in every conditional path or using a different structure:

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that handles the exception
    print("Cannot divide by zero.")
# No `finally` block here, so this code will not always run if there's an exception
print("This might not execute if an exception occurs.")
```
In this case, the code after the try-except block (`print("This might not execute if an exception occurs.")`) only runs if no exception is raised. If an exception is caught, the code after the except block is not executed.


## Custom Errors:
```python
a = int(input("Enter value between 5 & 9: "))
if a < 5 or a > 9:
   raise ValueError("Value should be 5 < x < 9 :)")
```
- Using the `raise` keyword to create custom errors.
- Useful when we want to do something specific when a particular exception is raised (e.g., sending an error report to admin, calling an API, etc.).

### Short-hand if-else:
```python
a = 330000
b = 3303

print("A") if a > b else print("=") if a == b else print("B")
c = 9 if a > b else 0
result = value_if_true if condition else value_if_false
```
- Used for simple if-else statements, especially when assigning a value to a variable based on a condition.

## Enumerate:
```python
marks = [12, 56, 32, 98, 12, 45, 1, 4]
index = 0
for mark in marks:
   print(mark)
   if index == 3:
      print("Awesome Aryab")
   index += 1
```

```python
for index, mark in enumerate(marks, start=1):
   print(index, mark)
   if index == 3:
      print("Awesome")
```
- Allows looping over a sequence (list, tuple, string) and getting the index and value of each element in the sequence at the same time.
- Useful when performing operations on both index and value.

```python
fruits = ['apple', 'banana', 'mango']
for idx, fruit in enumerate(fruits, start=1):
   print(idx, fruit)
```
```plaintext
# Output:
1 apple
2 banana
3 mango
```

## Virtual Environment:
- Isolates the Python environment to work on multiple projects with different versions, packages, and dependencies without conflict.
- Example: Project 1 uses OpenCV version 4.9.0, and another project uses OpenCV version 4.5.
- Commands:
  ```plaintext
  python -m venv env
  env/scripts/activate
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```
- Helps set up a project on the cloud or a new machine easily.
- Example to check version:
  ```python
  import pandas as pd
  print(pd.__version__)
  ```

## How Import Works:
- From `math` import `sqrt` as `s`:
  ```python
  from math import sqrt as s
  import math as math_builtin
  result = math_builtin.s(9) * math_builtin.pi
  ```

- `aryan.py`:
  ```python
  def welcome():
     print("Hey welcome!")

  aryan = "Good Boy"
  ```

- `main.py`:
  ```python
  from aryan import welcome
  ```

- Process of loading code from a module into the current script, allowing the use of functions and variables defined in the module.
- Example to import everything from `math`:
  ```python
  from math import *
  ```
- Renaming the imported module:
  ```python
  import math as m
  ```
- To list methods and properties:
  ```python
  import math
  print(dir(math))
  ```

## if `__name__ == "__main__"`:
- A common pattern in Python scripts to determine whether the script is being run directly or imported as a module in another script.

```python
def main():
   print("Running script directly")

if __name__ == "__main__":
   main()
```
- This pattern allows reusing code from a script by importing it as a module into another script without running the code in the original script.
- It helps in organizing and separating code that should be run directly from code that should be imported as a module. It allows determining whether the script is run directly or imported as a module in another script.
Sure, here's an improved and beautified markdown with outputs and some fixes:

---

## OS Module

```python
import os
if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")
```

- The `os` module is a built-in library that provides functions for interacting with the operating system.
- It allows for reading, writing files, running system commands, etc.

```python
f = os.open("file.txt", os.O_RDONLY)
g = os.open("gfile.txt", os.O_WRONLY)
contents = os.read(f, 1024)

os.write(g, b"hello")
os.close(f)
os.close(g)
```

- `os.listdir` -> Get a list of files in the directory

  ```python
  files = os.listdir(".")
  ```

- `mkdir` -> Create a new directory

- Running system commands:

  ```python
  os.system("color 2")
  ```

## Local & Global Variable

```python
x = 10
def my_function():
    global x
    x = 5  # Change variable of global var(x)
    y = 5  # Local variable

my_function()
print(x)  # Output: 5
print(y)  # Error: y is not accessible outside the function
```

> **Note:** Avoid modifying global variables within functions.

## File I/O

```python
f = open('myfile.txt', 'r')  # 'r' -> read mode
print(f)
text = f.read()
print(text)
f.close()
```

### Writing to a File

```python
f = open('myfile.txt', 'a')
f.write('hello world!')
f.close()
```

```python
with open('myfile.txt', 'a') as f:
    f.write("hey, I am inside")
```

### Modes:

1. **read (r)**: Opens & reads; gives error if file does not exist.
2. **write (w)**: Opens file for writing only and creates a new file if it does not exist.
3. **append (a)**: Appending only; creates a new file if it does not exist.
4. **create (x)**: Creates a new file and gives error if it already exists.
5. **text (t)**: Handles text files.
6. **binary (b)**: Used for binary files (images, PDFs).

> **Note:** Automatically close the file with the `with` keyword.

## Lambda Functions

```python
def appl(fx, value):  # fx = function
    return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))  # Output: 10
print(appl(lambda x: x * x, 2))  # Output: 10
```

- Small anonymous functions without a name.
- Syntax: `lambda arguments: expression`

Example:

```python
def multiply(x, y):
    return x * y

# LAMBDA equivalent
lambda x, y: x * y

lambda x, y: print(f"{x} * {y} = {x * y}")
```

## Map, Filter, Reduce

- Higher-order functions: Take other functions as arguments.

### Map

- Applies a function to each element in a sequence and returns a new sequence.

```python
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]
```

### Filter

- Filters a sequence of elements based on a given predicate (returns boolean value) and returns a new sequence containing only elements that meet the predicate.

```python
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]
```

### Reduce

- Applies a function to the first two elements in an iterable and then applies the function to the result and the next element, and so on.

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 15
```

## `is` vs `==`

```python
a = None
b = None
print(a is b)  # True: Both are None, the exact location of the object in memory

print(a is None)  # True
print(a == b)  # True: Values are the same
```

- Both are comparison operators.
- `is`: Compares the identity of objects.
- `==`: Compares the value of objects.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True: Same values
print(a is b)  # False: Different objects in memory
```

> **Note:** For strings and integers, `is` and `==` will return the same result.

## OOPS
# 4 Pillars of OOP
- **Inheritance**: Property Sharing
- **Encapsulation**: Data Hiding
- **Abstraction**: Simplified Interface
- **Polymorphism**: Multiple Forms

![image](https://github.com/user-attachments/assets/190068b0-7124-4380-8c52-1bf8b3643cf9)

### Object-Oriented Programming

- **Class**: A blueprint or template for creating objects.
  - **Properties**: Data/state of an object.
  - **Methods**: Actions that an object can perform.
- **Object**: An instance of a class, contains its own data and methods.
  
![image](https://github.com/user-attachments/assets/3cb4de84-7095-45b3-8e9f-8385c5c7e138)

## Encapsulation

- Internal state of an object is hidden and can only be accessed or modified through the object's methods.
- Helps in protecting the object's data and preventing it from being modified unexpectedly.

### Access Specifiers

- **Public Members**: Default; accessible from outside the class.
- **Protected Members**: Single underscore (`_`) prefix; intended for internal use within the class and its subclasses.
- **Private Members**: Double underscore (`__`) prefix; leads to name mangling, making it more challenging to access from outside the class.

## Abstraction

Abstraction is used to hide the internal functionality of the function from the users. Users interact with the basic implementation of the function, but the inner workings are hidden.

## Polymorphism

- Objects of different classes can be treated as if they were objects of a common class.
- Allows greater flexibility in code.
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Function to demonstrate polymorphism
def make_animal_speak(animal):
    print(animal.speak())

# Creating instances of different animals
dog = Dog()
cat = Cat()
bird = Bird()

# Demonstrating polymorphism
make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
make_animal_speak(bird) # Output: Tweet!
```
## Classes

A class is a blueprint or a template for creating objects providing initial values for state (member variables) and implementation of behavior (member functions or methods).

```python
class Details:
    name = "Aryan"
    age = 20
```

### Object: Instance of Class

```python
obj1 = Details()
print(obj1.name)  # Output: Aryan
print(obj1.age)  # Output: 20
```

### Self Parameter

- Reference to the current instance of the class.
- Used to access variables that belong to the class.

```python
class Details:
    name = "Aryan"
    age = 20

    def describe_person(self):
        print("My name is", self.name, "and I am", self.age, "years old")

obj1 = Details()
obj1.describe_person()
```

### Example

```python
class Person:
    name = "Aryan"
    occ = "SDE"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person()
b = Person()
c = Person()
a.name = "Shubh"
a.occ = "CA"
b.name = "Radhika"
b.occ = "HR"
a.info()  # Output: Shubh is a CA
b.info()  # Output: Radhika is an HR
c.info()  # Output: Aryan is an SDE
```


---

## Constructors

- Constructors are special methods in a class used to create and initialize an object of that class.
- They are unique functions that are invoked automatically when an object of a class is created.
- The main aim is to initialize or assign values to data members of the class.

```python
def __init__(self):
    # __init__ -> reserved function in Python
```

1. **Parameterized Constructors:**
    - When a constructor accepts arguments along with `self`.
    - These arguments can be used in the class to assign values to data members.

    ```python
    class Details:
        def __init__(self, animal, group):
            self.animal = animal
            self.group = group

    obj1 = Details("lion", "carnivores")
    print(obj1.animal, "belongs to", obj1.group)
    ```

2. **Default Constructors:**
    - When a constructor doesn't accept any arguments from the object and has only one argument - `self`.

    ```python
    class Details:
        def __init__(self):
            print("animal lion: carnivores")

    obj1 = Details()
    ```

## Decorators

- Python decorators are powerful and versatile tools that allow you to modify the behavior of functions and methods.
- They extend the functionality of functions without modifying their source code.
- A decorator takes another function as an argument and returns a new function that modifies the behavior of the original function.
- Hence, the new function is often referred to as the "decorated" function.

    ```python
    @decorator_function
    def my_function():
        pass
    ```

    ```python
    def smart_divide(func):
        def inner(a, b):
            print("I am going to divide", a, "and", b)
            if b == 0:
                print("Cannot divide")
                return
            return func(a, b)
        return inner

    @smart_divide
    def divide(a, b):
        print(a / b)

    divide(2, 5)
    # Output:
    # I am going to divide 2 and 5
    # 0.4
    ```

## Getters

- Getters in Python are methods used to access the values of an object's properties.
- They are used to return the value of a specific property and are defined using the `@property` decorator.

 ```python
    class MyClass:
        def __init__(self, value):
            self._value = value

        @property
        def value(self):
            return self._value

    obj = MyClass(10)
    print(obj.value)  # Output: 10
 ```

> **Note:** Getters do not take arguments and we cannot set the value through a getter method.

## Setters

```python
    class MyClass:
        def __init__(self, value):
            self._value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_val):
            self._value = new_val

    obj = MyClass(10)
    obj.value = 20
    print(obj.value)  # Output: 20
 ```

> **Note:** Setters are used for data encapsulation.

## Inheritance

- When a class derives from another class, the child class inherits all public and protected properties and methods from the parent class.
- In addition, it can have its own properties and methods. This is called inheritance.
- Derived classes inherit features from the base class, allowing for code reusability.

### Types of Inheritance:

1. **Single Inheritance**
2. **Multiple Inheritance**
3. **Multilevel Inheritance**
4. **Hierarchical Inheritance**
5. **Hybrid Inheritance**

   ![Inheritance Types](https://github.com/user-attachments/assets/6cb1cccb-f779-4f4e-b607-b7761010d9ff)

### Single Inheritance

- It enables a derived class to inherit properties from a single parent class.

 ```python
 class Parent:
     def func1(self):
         print("Parent Class")

 class Child(Parent):
     def func2(self):
         print("Child Class")

 obj = Child()
 obj.func1()  # Output: Parent Class
 obj.func2()  # Output: Child Class
 ```

### Multiple Inheritance

- When a class is derived from more than one base class, it is called multiple inheritance.
- All features of the base classes are inherited into the derived class.

 ```python
 class Mother:
     mothername = ""

     def mother(self):
         print(self.mothername)

 class Father:
     fathername = ""

     def father(self):
         print(self.fathername)

 class Son(Mother, Father):
     def parents(self):
         print(self.fathername)
         print(self.mothername)

 s1 = Son()
 s1.fathername = "Daddy"
 s1.mothername = "Mommy"
 s1.parents()
 ```

### Multilevel Inheritance

- Features of the base class and the derived class are further inherited into a new derived class.

 ```python
 class Grandfather:
     def __init__(self, grandfathername):
         self.grandfathername = grandfathername

 class Father(Grandfather):
     def __init__(self, fathername, grandfathername):
         Grandfather.__init__(self, grandfathername)
         self.fathername = fathername

 class Son(Father):
     def __init__(self, fathername, grandfathername, sonname):
         Father.__init__(self, fathername, grandfathername)
         self.sonname = sonname

     def print_name(self):
         print("Grandfather:", self.grandfathername)
         print("Father:", self.fathername)
         print("Son:", self.sonname)

 s1 = Son("Prince", "Ram", "Lal")
 s1.print_name()
 ```

### Hierarchical Inheritance

- When more than one derived class is created from a single base class, it is called hierarchical inheritance.

 ```python
 class Parent:
     def func1(self):
         print("Parent Class")

 class Child1(Parent):
     def func2(self):
         print("Child1")

 class Child2(Parent):
     def func3(self):
         print("Child2")

 obj1 = Child1()
 obj2 = Child2()
 obj1.func1()
 obj2.func1()
 obj1.func2()
 obj2.func3()
 ```

### Hybrid Inheritance

- Consists of multiple types of inheritance.

 ```python
 class School:
     def func1(self):
         print("School")

 class Student1(School):
     def func2(self):
         print("Student1")

 class Student2(School):
     def func3(self):
         print("Student2")

 class Student3(Student1, School):
     def func4(self):
         print("Function in Student3")

 obj1 = Student3()
 obj1.func1()
 obj1.func2()
 ```

## Access Modifiers or Specifiers

- Used to limit the access of class variables and methods outside of the class while implementing inheritance.

### Types:

1. **Public Access Modifiers**
2. **Private Access Modifiers**
3. **Protected Access Modifiers**

 ```python
 class Student:
     def __init__(self):
         self._name = "Harry"  # protected access modifier

     def _funName(self):  # protected method
         return "Aryan"

 class Subject(Student):
     pass

 obj = Student()
 obj1 = Subject()
 print(dir(obj))  # lists _funName, __init__, etc.

 # Calling by object of Student class
 print(obj._name)
 print(obj._funName())

 # Calling by object of Subject class
 print(obj1._name)
 print(obj1._funName())
 ```

- **Public Access Modifier:** All variables and methods are by default public.
    - `self.age = age` -> access publicly

- **Private Access Modifier:** Variables or methods are only accessible inside the class.
    - In Python, there's no concept of private access modifiers; however, by convention, variables prefixed with `__` are considered private.
    - Generally understood not to be used but still can.

 ```python
 class Student:
     def __init__(self, age, name):
         self.__age = age  # private variable

     def __funName(self):  # private function
         self.y = 34
         print(self.y)

 class Subject(Student):
     pass

 obj = Student(21, "Aryan")
 obj1 = Subject()

 # All below will give attribute error
 print(obj.__age)
 print(obj.__funName())
 print(obj1.__age)
 print(obj1.__funName())
 ```

> **How to access private variables?**: `*obj._Student__name*`

### Method Overriding

 ```python
 class Shape:
     def __init__(self, x, y):
         self.x = x
         self.y = y

     def area(self):
         return self.x * self.y

 class Circle(Shape):
     def __init__(self, r):
         self.r = r
         super().__init__(r, r)

     def area(self):
         return 3.14 * super().area()

 rec = Shape(3, 5)
 print(rec.area())

# Output: 15

 c = Circle(5)
 print(c.area())  # Output: 78.5
 ```

- Method overriding allows you to redefine a method in a derived class, overriding the method in the base class.
- When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed rather than the version in the base class.

---

# Static Methods 

Static methods belong to the class rather than an instance of the class.

- Defined using the `@staticmethod` decorator.
- Do not have access to the instance of the class (i.e., `self`).
- Used to create utility functions that don't need access to instance data.

```python
class Math:
   @staticmethod
   def add(a, b):
      return a + b

result = Math.add(1, 2)
print(result)  # Output: 3
```

---

# Class vs Instance Variables

- **Class variables** are shared among all instances of a class.  
  - Example: Used to store info that is common across all instances.

- **Instance variables** are unique to each instance of a class.  
  - Example: Used to store information specific to each instance.

**Accessing Variables:**
- Class variable: `ClassName.variable` or `self.__class__.variable`
- Instance variable: `self.variable_name`

```python
class Animal:
   species = "Mammal"  # Class variable

   def __init__(self, name):
      self.name = name  # Instance variable

a1 = Animal("Dog")
a2 = Animal("Cat")

print(a1.species)  # Output: Mammal
print(a2.name)     # Output: Cat
```

---

# Exercise: Clear Clutter Inside Folder (Rename PNG Files)

Rename all PNG images in a folder based on a sequence number (e.g., `1.png`, `2.png`).

```python
import os

files = os.listdir("clutter_folder")
i = 1
for file in files:
    if file.endswith(".png"):
        os.rename(f"clutter_folder/{file}", f"clutter_folder/{i}.png")
        i += 1
```

---

# Library Class Exercise

Create a `Library` class with two instance variables: `noBooks` (number of books) and `books`. Demonstrate adding books and printing the information.

```python
class Library:
   def __init__(self):
      self.noBooks = 0
      self.books = []

   def addBook(self, book):
      self.books.append(book)
      self.noBooks = len(self.books)

   def showInfo(self):
      print(f"No. of books: {self.noBooks}")
      for book in self.books:
         print(book)

l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("The Hobbit")
l1.showInfo()

# Output:
# No. of books: 2
# Harry Potter
# The Hobbit
```

---

# Python Class Methods

- **Class methods** are bound to the class and not the instance.
- Operates on the class as a whole rather than a specific instance.
- Defined using the `@classmethod` decorator.
- Useful for creating factory methods or alternative constructors.

```python
class Employee:
   company = "Apple"

   def show(self):
      print(f"Name: {self.name}, Company: {self.company}")

   @classmethod
   def changeCompany(cls, newCompany):
      cls.company = newCompany

e1 = Employee()
e1.name = "Aryan"
e1.show()  # Output: Name: Aryan, Company: Apple
Employee.changeCompany("Tesla")
e1.show()  # Output: Name: Aryan, Company: Tesla
```

---

# Class Methods as Alternative Constructors

```python
class Employee:
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary

   @classmethod
   def fromStr(cls, string):
      name, salary = string.split("-")
      return cls(name, int(salary))

e1 = Employee("Aryan", 1200)
print(e1.name)     # Output: Aryan
print(e1.salary)   # Output: 1200

e2 = Employee.fromStr("John-1500")
print(e2.name)     # Output: John
print(e2.salary)   # Output: 1500
```

---

# Useful Methods: `dir()`, `__dict__`, and `help()`

- **`dir()`**: Returns a list of attributes and methods, including special methods.
- **`__dict__`**: Returns a dictionary representation of an object's attributes.
- **`help()`**: Displays help documentation for an object.

```python
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

p = Person("John", 30)
print(p.__dict__)   # Output: {'name': 'John', 'age': 30}
print(dir(p))       # Output: ['__class__', '__delattr__', ...] 
```

---

## Super Keyword

- The `super()` function is used to refer to the parent class.
- Useful in class inheritance to extend the behavior of a method from the parent class.

```python
class Employee:
   def __init__(self, name, id):
      self.name = name
      self.id = id

class Programmer(Employee):
   def __init__(self, name, id, lang):
      super().__init__(name, id)
      self.lang = lang

harry = Programmer("Harry", 23, "Python")
print(harry.name)  # Output: Harry
print(harry.lang)  # Output: Python
```

---

## Dunder (Magic) Methods

- Special methods that customize the behavior of classes.
- Example: Implementing addition, comparison operators, etc.

1. **`__init__`**: Called when a new instance is created (constructor).
2. **`__str__` & `__repr__`**: Convert objects to string.
3. **`__len__`**: Returns the length of an object.
4. **`__call__`**: Makes an object callable like a function.

```python
class Employee:
   def __init__(self, name):
      self.name = name

   def __len__(self):
      return len(self.name)

   def __str__(self):
      return f"Employee: {self.name}"

   def __repr__(self):
      return f"Employee({self.name})"

   def __call__(self):
      print(f"Hello, I am {self.name}")

e = Employee("Aryan")
print(len(e))      # Output: 5
print(str(e))      # Output: Employee: Aryan
e()                # Output: Hello, I am Aryan
```

---

## Method Overriding

- Allows you to redefine a method in a derived class.
- When you call an overridden method, the derived class method is executed.

```python
class Shape:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def area(self):
      return self.x * self.y

class Circle(Shape):
   def __init__(self, r):
      super().__init__(r, r)

   def area(self):
      return 3.14 * super().area()

rect = Shape(3, 5)
print(rect.area())  # Output: 15

circle = Circle(5)
print(circle.area())  # Output: 78.5
```

---

## Operator Overriding

- Allows you to redefine the behavior of mathematical and comparison operators for custom data types.
- Example: Adding two `Vector` objects.

```python
class Vector:
   def __init__(self, i, j, k):
      self.i = i
      self.j = j
      self.k = k

   def __add__(self, other):
      return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

   def __str__(self):
      return f"{self.i}i + {self.j}j + {self.k}k"

v1 = Vector(3, 5, 6)
v2 = Vector(1, 2, 9)
v3 = v1 + v2
print(v3)  # Output: 4i + 7j + 15k
```

> **Note:** `super()` is helpful in extending the behavior of a base class method rather than replacing it entirely.
---


# **Exercise: Merge PDFs into a Single PDF**

```python
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("Merged-pdf.pdf")
merger.close()
```

Output:
- Merges all the PDF files in the current directory into a single file named `Merged-pdf.pdf`.

---

# **Time Module:**

- **Provides a set of functions to work with time-related operations such as timekeeping, formatting, and time conversions.**
- **Common Functions:**

  - **`time.time()`**: Returns the current time in seconds since the Epoch (1970).
    
    **Example:**
    ```python
    import time
    start_time = time.time()
    print("Current Time:", start_time)
    ```

  - **`time.sleep(seconds)`**: Suspends the execution of the current thread for a specific number of seconds.
    
    **Example:**
    ```python
    import time
    print("Start")
    time.sleep(2)
    print("End after 2 seconds")
    ```

  - **`time.strftime()`**: Formats a time value as a string based on a specific format.
    
    **Example:**
    ```python
    import time
    t = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d, %H:%M:%S", t)
    print(formatted_time)
    ```

---

# **Command Line Utility:**

- **Command-line programs are essential for automating tasks and working efficiently in development workflows.**

### **Basic Example:**

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1", help="Description of Arg1")
parser.add_argument("arg2", help="Description of Arg2")
args = parser.parse_args()

print(args.arg1)
print(args.arg2)
```

### **File Downloader Example:**

```python
import argparse
import requests
import shutil

def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    response = requests.get(url, stream=True)
    with open(local_filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a file from a URL")
    parser.add_argument("url", help="URL of the file")
    parser.add_argument("output", help="Output filename")
    args = parser.parse_args()
    download_file(args.url, args.output)
    print("File downloaded:", args.output)
```

Output:
- Downloads a file from the provided URL and saves it with the specified output name.

---

# **Walrus Operator (`:=`):**

- **Introduced in Python 3.8, the Walrus Operator allows assignment within expressions.**

### **Example:**

```python
happy = False
print("Before:", happy)
print("After:", happy := True)

foods = list()
while (food := input("What food do you like? ")) != "quit":
    foods.append(food)

print("Foods you like:", foods)
```

---

# **`shutil` Module:**

- **A high-level file operation utility in Python.**

### **Functions:**

- **`shutil.copy(src, dst)`**: Copies the file.
- **`shutil.copy2(src, dst)`**: Copies the file along with metadata.
- **`shutil.copytree(src, dst)`**: Recursively copies a directory.
- **`shutil.move(src, dst)`**: Moves a file or directory.
- **`shutil.rmtree(path)`**: Deletes a directory tree.

---

# **Beautiful Soup (bs4): Web Scraping**

- **Beautiful Soup is a Python library for web scraping purposes.**
  
```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())

for heading in soup.find_all("h1"):
    print(heading.text)
```

Output:
- Prints the entire webpage content in a structured format and all `<h1>` headings.

---

# **Generators:**

- **Generators are special types of functions that allow you to iterate over values one by one without creating a full list in memory.**

### **Example:**

```python
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))  # Output: 0

for j in gen:
    print(j)  # Output: 1, 2, 3, 4
```

---

# **Function Caching (`@lru_cache`):**

- **Caches function results to avoid recomputation for the same inputs, useful for expensive calculations.**

### **Example:**

```python
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)  # Simulate a slow function
    return n * 5

print(fx(20))  # First call, takes 5 seconds
print(fx(2))   # First call, takes 5 seconds
print(fx(6))   # First call, takes 5 seconds

# Cached calls, output is immediate
print(fx(20))
print(fx(2))
print(fx(6))
```

---

# **Regular Expressions (Regex):**

- **A powerful tool for matching and manipulating strings using patterns.**

### **Basic Regex:**

```python
import re
pattern = r"expression"
text = "hello world!"
match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("No match found.")
```

### **Example:**

```python
import re

text = "The cat is in the hat"
pattern = r"[a-z]+at"
matches = re.findall(pattern, text)
print("Matches:", matches)  # Output: ['cat', 'hat']

new_text = re.sub(pattern, "dog", text)
print("Updated text:", new_text)  # Output: "The dog is in the dog"
```

### **Extracting Emails:**

```python
import re

text = "Email ID is example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    email = match.group()
    print("Extracted Email:", email)
```

# AsyncIO
- Allows for high-performance I/O operations in a concurrent and non-blocking manner.
- Module: `asyncio`

```python
import asyncio
import requests

async def function1():
    url = "https://example.com/wallpaper.jpg"
    response = requests.get(url)
    open("instagram.ico", "wb").write(response.content)
    return "aryan"

async def function2():
    url = "https://example.com/preview.jpg"
    response = requests.get(url)
    open("insta2.png", "wb").write(response.content)

async def main():
    l = await asyncio.gather(function1(), function2())
    print(l)

asyncio.run(main())
```

### Output:
- **instagram.ico** and **insta2.png** will be downloaded.
- The list `['aryan', None]` will be printed.

---

# MultiThreading
- Allows multiple threads of execution to run concurrently within a single process.
- In Python, we use the `threading` module to implement multithreading.
- Create a thread -> call its `start()` method.
- `join()` stops execution until the thread completes.

```python
import threading

def my_func():
    print("Hello from thread", threading.current_thread().name)

thread = threading.Thread(target=my_func)
thread.start()
thread.join()
```

### Output:
- `Hello from thread Thread-1` (or similar, depending on the thread name).

### Functions:
1. **`threading.Thread(target, args)`**:
   - Creates a new thread that runs the target function with arguments.
   
2. **`threading.Lock()`**:
   - Creates a lock that can be used to synchronize access to shared resources between threads.
   - A lock ensures that only one thread can execute a critical section at a time.

### Example with Lock:

```python
import threading

def increment(counter, lock):
    for i in range(100):
        lock.acquire()
        counter[0] += 1
        lock.release()

if __name__ == "__main__":
    counter = [0]  # List is used to allow modification in thread
    lock = threading.Lock()
    threads = []

    for i in range(2):
        thread = threading.Thread(target=increment, args=(counter, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter[0]}")
```

### Output:
- The final counter value will be `200`.

---

# Using ThreadPoolExecutor

```python
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    time1 = time.perf_counter()

    # Using threads
    with ThreadPoolExecutor() as executor:
        t1 = executor.submit(func, 4)
        t2 = executor.submit(func, 2)
        t3 = executor.submit(func, 1)

        print(t1.result())
        print(t2.result())
        print(t3.result())

    time2 = time.perf_counter()
    print(f"Finished in {time2 - time1} seconds")

main()
```

### Output:
- Threads will print sleep statements and the total time taken will be reduced since the threads run concurrently.

---

# Multiprocessing
- A module in Python that provides a way to run multiple processes in parallel.
- Allows you to take advantage of multiple cores/processors on the system, which can significantly improve the performance of code.

```python
import concurrent.futures
import requests
import os

def download_file(url, name):
    try:
        print(f"Started downloading {name}")
        response = requests.get(url)
        file_path = f"{name}.jpg"
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Finished downloading {name}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    with concurrent.futures.ProcessPoolExecutor() as executor:
        pros = []
        for i in range(50):
            pros.append(executor.submit(download_file, url, f"image_{i}"))

        for future in concurrent.futures.as_completed(pros):
            future.result()
```

### Output:
- The script will download 50 images concurrently.

---

# Multiprocessing vs Multithreading

| **S.No** | **Multiprocessing**                                              | **Multithreading**                                               |
|----------|-------------------------------------------------------------------|------------------------------------------------------------------|
| 1.       | CPUs are added for increasing computing power.                    | Many threads are created of a single process for concurrency.    |
| 2.       | Many processes are executed simultaneously.                       | Many threads of a process are executed simultaneously.           |
| 3.       | Classified into Symmetric and Asymmetric multiprocessing.         | Not classified into categories.                                  |
| 4.       | Process creation is time-consuming.                               | Thread creation is more economical.                              |
| 5.       | Every process owns a separate address space.                      | A common address space is shared by all the threads.             |
