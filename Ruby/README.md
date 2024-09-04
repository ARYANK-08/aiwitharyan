# Ruby Programming Language

![image](https://github.com/user-attachments/assets/c17326f4-97d3-43da-83c1-60c30665cb67)

# Table of Contents

| Topic Name                                    | Link                                    |
|-----------------------------------------------|-----------------------------------------|
| 🧩 Variables in Ruby  | [Variables in Ruby](#variables-in-ruby)  |
| 🔢 Data Types                | [Data Types](#data-types)    |
| 🔠 Working with Strings | [Working with Strings](#working-with-strings) |
| ➕ Math and Numbers       | [Math and Numbers](#math-and-numbers)   |
| 🛠️ Defining and Calling Methods]| [Defining and Calling Methods](#defining-and-calling-methods)|
| 📝 Conditional Statements] | [Conditional Statements](#conditional-statements) |
| 🔄 While Loop]            | [While Loop](#while-loop) |
| 🧑‍🎓 Classes and Objects] | [Classes and Objects](#classes-and-objects) |
| 🏛️ Inheritance]              | [Inheritance](#inheritance)|





Ruby is a dynamic, open-source programming language with a focus on simplicity and productivity. It features an elegant syntax that is natural to read and easy to write. Ruby can be used for a variety of applications, including:

- Web applications
- E-commerce platforms
- Content management systems
- Custom database solutions
- Prototyping
- And more

tbh : ruby is very similar to python in terms of syntax except (:) xD

## Examples and Explanations

### Demonstrating `puts` vs. `print`

```ruby
# `puts` adds a newline after output
# `print` does not add a newline
puts "Aryan"
print "is cool"
```

**Output:**
```
Aryan
is cool
```

**Explanation:**
- `puts` will add a new line after the output.
- `print` will keep the output on the same line.

### Ruby Code Execution

```ruby
# When Ruby runs, it executes instructions line by line,
# moving to the next line after completing each instruction.
```

### Variables in Ruby

```ruby
character_name = "Aryan"
character_age = "35"
puts character_age

puts "My name is " + character_name
puts "I am " + character_age + " years old"
```

**Explanation:**
- Variables store pieces of information.
- Example: Modifying info like name and age manually in a string.

### Data Types

1. **String**: Plain text
   ```ruby
   name = "Aryan"
   occupation = "programmer"
   ```

2. **Numbers**:
   ```ruby
   age = 20         # Integer
   gpa = 9.3        # Floating point number
   ```

3. **Boolean**:
   ```ruby
   is_male = true
   is_tall = false
   ```

4. **Nil**:
   ```ruby
   flaws = nil
   ```

### Working with Strings

```ruby
phrase = "Giraffe Academy"
puts phrase[-1]          # Output: "y"
puts phrase.index("ffe") # Output: 6
```

**String Methods:**
```ruby
phrase = "   Hello World!   "

puts phrase.upcase()   # Output: "   HELLO WORLD!   "
puts phrase.downcase() # Output: "   hello world!   "
puts phrase.strip()    # Output: "Hello World!"
puts phrase.length()   # Output: 16
puts phrase.include?("World") # Output: true
puts phrase[1]         # Output: " "
puts phrase.index("World") # Output: 7
```

### Math and Numbers

```ruby
num = 20.2
puts "My favorite number is " + num.to_s
puts num.round()  # Output: 20
puts num.ceil()   # Output: 21
puts num.floor()  # Output: 20

puts Math.sqrt(4) # Output: 2.0
puts Math.log(1)  # Output: 0.0
```

**Math Operations:**
```ruby
# Basic arithmetic
puts 5 + 3     # Output: 8
puts 5 - 3     # Output: 2
puts 5 * 3     # Output: 15
puts 5 / 3     # Output: 1

# Exponentiation and modulus
puts 5 ** 2    # Output: 25
puts 5 % 2     # Output: 1
```

**Conversion and Rounding Methods:**
- `to_s` - Convert to string
- `round` - Round to the nearest integer
- `ceil` - Round up to the nearest integer
- `floor` - Round down to the nearest integer

**Mathematical Functions:**
- `Math.sqrt(x)` - Square root of `x`
- `Math.log(x)` - Natural logarithm of `x`


## Getting Input from the User

```ruby
# Getting input from the user
puts "Enter your name: "
user_name = gets.chomp
puts "Enter your age: "
user_age = gets.chomp
puts "Your name is #{user_name} and your age is #{user_age}. You are cool!"
```

**Explanation:**
- `gets.chomp` reads input from the user and removes the newline character.
- `#{}` is used for string interpolation to include variable values within a string.

## Building a Calculator

```ruby
# Building a simple calculator
puts "Enter a number: "
num1 = gets.chomp # Gets input and removes newline
puts "Enter another number: "
num2 = gets.chomp

# Concatenates two strings (not correct for numbers)
puts num1 + num2

# Convert strings to integers and floats for addition
puts (num1.to_i + num2.to_i) # Addition of integers
puts (num1.to_f + num2.to_f) # Addition of decimal numbers
```

**Explanation:**
- `to_i` converts a string to an integer.
- `to_f` converts a string to a float.

## Building a Mad Libs Game

```ruby
# Building a Mad Libs game
puts "Enter a color:"
color = gets.chomp
puts "Enter a plural noun:"
noun = gets.chomp
puts "Enter a description:"
desc = gets.chomp

puts "Roses are #{color}"
puts "Violets are #{noun}"
puts "The one who does DSA is a #{desc}"
```

**Explanation:**
- This example uses string interpolation to create a playful text.

## Arrays

Arrays are ordered, integer-indexed collections of any object.

```ruby
# Creating and manipulating arrays
friends = ["Pradyumnaa", "Myron", "Sharvin"] # Array with different data types
puts friends           # Outputs entire array
puts friends[0]        # Outputs the first element
puts friends[-1]       # Outputs the last element
puts friends[0, 2]     # Outputs elements from index 0 to 2 (exclusive)

# Modifying an array
friends[0] = "Aditya"
puts friends[0]        # Outputs the modified first element
puts friends           # Outputs entire array

# Working with an empty array
friends = Array.new
friends[0] = "Aryan"
friends[1] = "Myron"

puts friends.length()  # Outputs the length of the array
puts friends.include?("Aryan")  # Checks if "Aryan" is in the array
puts friends.reverse() # Outputs the array in reverse order
puts friends.sort()    # Outputs the array sorted alphabetically
print friends          # Prints the entire array without new lines
```

## Hashes

Hashes are collections of key-value pairs, similar to dictionaries in other languages.

```ruby
# Creating and using hashes
states = {
  "New York" => "NY",
  "Pennsylvania" => "PA",
  "California" => "CA", # Corrected abbreviation
  :Maharashtra => "MH"  # Symbol as a key
}

puts states["New York"] # Outputs the value associated with the key "New York"
```

**Explanation:**
- Hashes are used to store data in key-value pairs.
- You can use symbols (`:key`) or strings (`"key"`) as keys.


# Ruby Methods

## Methods (Functions)

Methods in Ruby are blocks of code that perform specific tasks. They can accept parameters and return values.

### Defining and Calling Methods

```ruby
# Basic method definition
def say_hi
  puts "Hello User"
end

say_hi # Calls the method
```

**Output:**
```
Hello User
```

### Methods with Parameters

```ruby
# Method with parameters
def say_hi_to(name, age)
  puts "Hello #{name}, your age is #{age}"
end

say_hi_to("Aryan", "20")
```

**Output:**
```
Hello Aryan, your age is 20
```

### Methods with Default Parameter Values

```ruby
# Method with default parameter values
def say_hi_to1(name="no name", age=-1)
  puts "Hello #{name}, your age is #{age}"
end

say_hi_to1("Aryan")
```

**Output:**
```
Hello Aryan, your age is -1
```

### Returning Values from Methods

```ruby
# Method that returns a value
def cube_number(number)
  cubed_value = number**3
  return cubed_value
end

puts cube_number(2)
```

**Output:**
```
8
```

## Conditional Statements

Conditional statements allow you to execute code based on certain conditions.

### Basic `if` Statement

```ruby
# Basic if statement
grind = false 
if grind
  puts "Grind is ON!"
else
  puts "Start the GRIND ASAP!"
end 
```

**Output:**
```
Start the GRIND ASAP!
```

### Multiple Conditions with `if` Statements

```ruby
# Multiple conditions
dsa_grind = true
dev_grind = false

if dsa_grind && dev_grind
  puts "Cracked Coder"
elsif dsa_grind && !dev_grind
  puts "Mega noob Coder"
elsif dev_grind && !dsa_grind
  puts "Cool Coder"
else
  puts "Noob Coder"
end
```

**Output:**
```
Mega noob Coder
```

### Using Comparisons in `if` Statements

```ruby
# Method to find the greatest number
def max_number(n1, n2, n3)
  if n1 >= n2 && n1 >= n3
    puts "n1 is the greatest"
    return n1
  elsif n2 >= n1 && n2 >= n3
    puts "n2 is the greatest"
    return n2
  else
    puts "n3 is the greatest"
    return n3
  end
end

puts max_number(10, 20, 30)
```

**Output:**
```
n3 is the greatest
30
```

### Comparison Operators

Ruby supports various comparison operators:
- `!=` (not equal)
- `==` (equal)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)

## Building a Simple Calculator

```ruby
# Calculator method
def calculator
  # Get the first number from user input
  puts "Enter the first number:"
  num1 = gets.chomp.to_i

  # Get the second number from user input
  puts "Enter the second number:"
  num2 = gets.chomp.to_i

  # Get the user's choice of operation
  puts "Enter 1: add, 2: sub, 3: mul, 4: div"
  user_input = gets.chomp

  # Perform the chosen operation using if statements
  if user_input == "1"
    puts num1 + num2
  elsif user_input == "2"
    puts num1 - num2
  elsif user_input == "3"
    puts num1 * num2
  elsif user_input == "4"
    if num2 == 0
      puts "Cannot divide by zero"
    else
      puts num1.to_f / num2
    end
  else
    puts "Invalid input"
  end
end

calculator
```

**Explanation:**
- This method allows the user to perform basic arithmetic operations by entering numbers and choosing an operation.
- Handles division by zero and invalid inputs.

**Example Usage:**
```
Enter the first number:
5
Enter the second number:
3
Enter 1: add, 2: sub, 3: mul, 4: div
1
8
```

## Case Statement

A `case` statement in Ruby is used for conditional logic based on the value of a variable. Here’s an example that converts a shorthand day name to a full day name.

```ruby
def get_day_name(day)
  day_name = ""

  case day
  when "mon"
    day_name = "Monday"
  when "tue"
    day_name = "Tuesday"
  when "wed"
    day_name = "Wednesday"
  when "thurs"
    day_name = "Thursday"
  when "fri"
    day_name = "Friday"
  when "sat"
    day_name = "Saturday"
  when "sun"
    day_name = "Sunday"
  else
    day_name = "Invalid day"
  end 

  return day_name
end

puts get_day_name(gets.chomp())
```

**Example:**
```
Input: "fri"
Output: "Friday"
```

## While Loop

The `while` loop repeats a block of code as long as a given condition is true. Here are some examples:

### Simple While Loop

Print numbers from `0` to `4`.

```ruby
i = 0
while i < 5
  puts i
  i += 1
end
```

**Output:**
```
0
1
2
3
4
```

### While Loop with Conditional Printing

Print even numbers from `0` to `11`.

```ruby
i = 0
while i < 12
  puts i if i % 2 == 0
  i += 1
end
```

**Output:**
```
0
2
4
6
8
10
```

**Note:** Ensure the loop condition will eventually become false to avoid infinite loops.

## Guessing Game

A simple guessing game where the user has to guess a secret word within 10 attempts.

```ruby
secret_word = "godlevel"
guess = ""
guess_count = 0

while guess != secret_word && guess_count < 10
  puts "Enter the guess word:"
  guess = gets.chomp
  guess_count += 1
  puts "Guesses left: #{10 - guess_count}"
end

if guess_count < 10
  puts "You guessed it in #{guess_count} attempts!"
else
  puts "You lost! The correct word was '#{secret_word}'."
end
```

**Example:**
```
Input: "godlevel"
Output: "You guessed it in 1 attempts!"
```

## For Loops

### Iterating Over an Array

Print each name from an array of friends.

```ruby
friends = ["Aryan", "Myron", "Sharvin", "Pradyumnaa"]

for friend in friends
  puts friend
end
```

**Output:**
```
Aryan
Myron
Sharvin
Pradyumnaa
```

### Using a Range

Print numbers from `0` to `5`.

```ruby
for i in 0..5
  puts i
end
```

**Output:**
```
0
1
2
3
4
5
```

### Using Times Iterator

Print numbers from `0` to `5` using the `times` iterator.

```ruby
6.times do |index|
  puts index
end
```

**Output:**
```
0
1
2
3
4
5
```

## Building an Exponent Method

Calculate the exponent of a base number.

```ruby
def expo(base, power)
  result = 1
  power.times do
    result *= base
  end
  return result
end

puts expo(5, 2)
```

**Output:**
```
25
```

## Comments

Comments are used to explain code or temporarily disable it.

```ruby
# This is a single-line comment

=begin
This is a multi-line comment.
It can span multiple lines.
=end
```

## Reading Files

Read from a file and print its content.

```ruby
File.open("emp.txt", "r") do |file|
  puts file.readlines()[2] # Print the third line
  file.each do |line|
    puts line # Print each line
  end
end
```

**Example Content of `emp.txt`:**
```
Aryan, Tech
Myron, QA
Pradyumnaa, CyberSecurity
Sharvin, Masters
```

**Output:**
```
Pradyumnaa, CyberSecurity
Myron, QA
Pradyumnaa, CyberSecurity
Sharvin, Masters
```

**Modes:** 
- `"r"`: Read mode
- `"w"`: Write mode
- `"r+"`: Read and write mode

**Methods:**
- `file.readline` - Reads one line at a time.
- `file.readchar` - Reads a single character.

---


## Writing to Files

### Append Mode (`"a"`)

Use `"a"` mode to open a file for appending data. This will add new content to the end of the file without affecting existing content.

```ruby
File.open("emp.txt", "a") do |file|
  file.write("\nTanjiro, Anime")  # Append new employee
end
```

**Explanation:** 
- Opens `emp.txt` in append mode.
- Adds `"Tanjiro, Anime"` to the end of the file.

**Example Content of `emp.txt` After Execution:**
```
Aryan, Tech
Myron, QA
Pradyumnaa, CyberSecurity
Sharvin, Masters
Tanjiro, Anime
```

### Read and Write Mode (`"r+"`)

Use `"r+"` mode to open a file for both reading and writing. This will start at the beginning of the file and can overwrite existing content if not handled carefully.

```ruby
File.open("emp.txt", "r+") do |file|
  file.write("Tanjiro, Anime")  # Overwrite content from the beginning
end
```

**Explanation:** 
- Opens `emp.txt` in read and write mode.
- Overwrites the file's content starting from the beginning.

**Example Content of `emp.txt` After Execution:**
```
Tanjiro, Anime
```

### Write Mode (`"w+"`)

Use `"w+"` mode to open a file for both reading and writing. If the file already exists, its contents are truncated (cleared). If it doesn’t exist, a new file is created.

```ruby
File.open("emp.txt", "w+") do |file|
  file.write("Tanjiro, Anime")  # Write new content, file is cleared first
end
```

**Explanation:** 
- Opens `emp.txt` in write and read mode.
- Clears the file and writes `"Tanjiro, Anime"`.

**Example Content of `emp.txt` After Execution:**
```
Tanjiro, Anime
```

## Exception Handling

Ruby uses `begin` and `rescue` blocks to handle exceptions and errors gracefully.

### Basic Exception Handling

```ruby
begin
  puts 2 / 0  # This will raise a ZeroDivisionError
rescue
  puts "Division by zero error"  # Handle the exception
end
```

**Explanation:**
- `begin` starts the block of code that may raise an exception.
- `rescue` handles the exception if it occurs.

**Output:**
```
Division by zero error
```

### Handling Specific Exceptions

```ruby
nums = [1, 2, 3, 4]
begin
  puts nums["doh1"]  # This will raise a TypeError
rescue TypeError
  puts "Wrong Type"  # Handle TypeError specifically
rescue ZeroDivisionError
  puts "Division by zero error"  # Handle ZeroDivisionError specifically
rescue TypeError => e
  puts e  # Handle TypeError and print the error message
end
```

**Explanation:**
- Handles `TypeError` and `ZeroDivisionError` separately.
- `rescue TypeError => e` captures the exception and prints its message.

**Output:**
```
Wrong Type
```

# Ruby Classes and Inheritance

## Classes and Objects

In Ruby, a class is a blueprint for creating objects. Objects are instances of classes and can hold data and methods.

### Defining a Class

```ruby
class Book
  attr_accessor :title, :author, :pages  # Attributes for the Book class

  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end
end

book1 = Book.new("Harry Potter", "JK Rowling", 400)
puts book1.title   # Output: Harry Potter

book2 = Book.new("What You Call a Python Living?", "Aryan", 100)
puts book2.author  # Output: Aryan
```

**Explanation:**
- `attr_accessor` creates getter and setter methods for the attributes.
- `initialize` method is used to set initial values for the object’s attributes.

## More Examples of Classes

### Student Class

```ruby
class Student
  attr_accessor :name, :major, :gpa

  def initialize(name, major, gpa)
    @name = name
    @major = major
    @gpa = gpa
  end

  def has_honors?
    @gpa >= 9.0
  end
end

student1 = Student.new("Myron", "AI", 9.6)
student2 = Student.new("Aryan", "CS", 9.5)

puts student1.has_honors?  # Output: true
puts student2.has_honors?  # Output: true
```

### Question Class for a Quiz

```ruby
class Question
  attr_accessor :prompt, :answer

  def initialize(prompt, answer)
    @prompt = prompt
    @answer = answer
  end
end

p1 = "What color are apples?\n(a).red\n(b).purple\n(c).yellow\n(d).orange"
p2 = "What color are bananas?\n(a).red\n(b).purple\n(c).yellow\n(d).orange"
p3 = "What color are pears?\n(a).red\n(b).green\n(c).yellow\n(d).orange"

questions = [
  Question.new(p1, "a"),
  Question.new(p2, "c"),
  Question.new(p3, "b")
]

def run_test(questions)
  score = 0
  questions.each do |question|
    puts question.prompt
    answer = gets.chomp
    score += 1 if answer == question.answer
  end
  puts "You got #{score} / #{questions.length}"
end

run_test(questions)
```

**Explanation:**
- The `Question` class represents a question with a prompt and an answer.
- `run_test` method iterates through questions, prompts the user, and calculates the score.

## Inheritance

Inheritance allows a class to inherit features from another class, promoting code reuse and extending functionality.

### Basic Inheritance Example

```ruby
class Chef
  def make_chicken
    puts "Chef makes chicken"
  end

  def make_salad
    puts "Chef makes salad"
  end

  def make_special_dish
    puts "Chef makes BBQ"
  end
end

class ItalianChef < Chef
  def make_special_dish
    puts "Italian Chef makes Paneer Tikka"
  end

  def make_pasta
    puts "Italian Chef makes Pasta"
  end
end

chef = Chef.new
chef.make_chicken      # Output: Chef makes chicken

italian_chef = ItalianChef.new
italian_chef.make_salad       # Output: Chef makes salad
italian_chef.make_special_dish  # Output: Italian Chef makes Paneer Tikka
```

**Explanation:**
- `ItalianChef` inherits from `Chef` and overrides the `make_special_dish` method.
- `ItalianChef` also adds a new method `make_pasta`.

## Types of Inheritance

### 1. **Single Inheritance**

A class inherits from one parent class. This is the most common form of inheritance.

```ruby
class Animal
  def speak
    puts "Animal speaks"
  end
end

class Dog < Animal
  def bark
    puts "Dog barks"
  end
end

dog = Dog.new
dog.speak  # Output: Animal speaks
dog.bark   # Output: Dog barks
```

### 2. **Multiple Inheritance (Through Mixins)**

Ruby does not support multiple inheritance directly but allows a form of it using modules.

```ruby
module Swimmer
  def swim
    puts "Swimming"
  end
end

module Flyer
  def fly
    puts "Flying"
  end
end

class Duck
  include Swimmer
  include Flyer
end

duck = Duck.new
duck.swim  # Output: Swimming
duck.fly   # Output: Flying
```

**Explanation:**
- Modules `Swimmer` and `Flyer` are mixed into the `Duck` class, allowing it to have both functionalities.

### 3. **Hierarchical Inheritance**

Multiple classes inherit from the same parent class.

```ruby
class Animal
  def breathe
    puts "Breathing"
  end
end

class Bird < Animal
  def fly
    puts "Flying"
  end
end

class Fish < Animal
  def swim
    puts "Swimming"
  end
end

bird = Bird.new
fish = Fish.new
bird.breathe  # Output: Breathing
fish.breathe  # Output: Breathing
```

**Explanation:**
- Both `Bird` and `Fish` inherit from `Animal` and share the `breathe` method.
Here's an explanation of different types of inheritance in Ruby, along with examples. I've also included an explanation of the `module` and `require_relative` concepts, and a brief on Interactive Ruby (IRB).

---

## Modules

Modules in Ruby are a way to group related methods, classes, or constants. They cannot be instantiated but can be included in other classes to share functionality.

### Example of a Module

#### `file.rb`:
```ruby
module Tools
  def say_hi(name)
    puts "Hello #{name}"
  end

  def say_bye(name)
    puts "Bye #{name}"
  end
end
```

**Explanation:**
- `Tools` module defines two methods: `say_hi` and `say_bye`.

### Using Modules in Your Code

#### Main File:
```ruby
require_relative "file"  # Include the module from file.rb
include Tools

say_hi("Aryan")  # Output: Hello Aryan
say_bye("Aryan") # Output: Bye Aryan
```

**Explanation:**
- `require_relative "file"` tells Ruby to load the `file.rb` file.
- `include Tools` makes the `Tools` module's methods available in the current context.
- The methods `say_hi` and `say_bye` can now be used directly.

## Interactive Ruby (IRB)

IRB (Interactive Ruby) is a REPL (Read-Eval-Print Loop) environment for Ruby. It allows you to execute Ruby code interactively and is useful for testing snippets of code and experimenting with Ruby.

### Example:

```bash
$ irb
> puts "Hello, world!"
Hello, world!
> 2 + 2
=> 4
```

**Explanation:**
- Start IRB from the command line by typing `irb`.
- You can enter Ruby code directly, and IRB will execute it and display the result immediately.

---

thanks for reading :) 

![5283106](https://github.com/user-attachments/assets/be6a4ebf-2a1a-4570-92f5-0e01d7428b75)

