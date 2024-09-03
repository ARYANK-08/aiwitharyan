# 🤖 #aiwitharyan

# Ruby Programming Language

Ruby is a dynamic, open-source programming language with a focus on simplicity and productivity. It features an elegant syntax that is natural to read and easy to write. Ruby can be used for a variety of applications, including:

- Web applications
- E-commerce platforms
- Content management systems
- Custom database solutions
- Prototyping
- And more

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

