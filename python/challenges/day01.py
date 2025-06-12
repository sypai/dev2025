"""
Challenge 01:

Write a snippet that:

Accepts a variable x

Checks if it’s an int, float, str, or list

Prints a message like "x is an integer" or "x is a string"
"""
def challenge_01():
    x = input("Enter something...")
    if isinstance(x, int):
        print("x is an integer")
    elif isinstance(x, float):
        print("x is a float")
    elif isinstance(x, str):
        print("x is a string")
    elif isinstance(x, list):
        print("x is a list")
    else:
        print("Unknown type")
    print(" --- --- --- ")

"""
Challenge 02:
Write a function describe_input() that:

Takes an input using input()

Tries to convert it to int, then float, else leaves it as a string

Prints the type and value in a sentence like:

You entered a float: 3.14
"""
def describe_input():
    user_input = input("Enter something: ")
    try:
        value = int(user_input)
        print(f"You entered an integer: {value}")
    except ValueError:
        try:
            value = float(user_input)
            print(f"You entered a float: {value}")
        except ValueError:
            print(f"You entered a string: {user_input}") 
    print(" --- --- --- ")


"""
Challenge 03

Write a function math_summary(a, b) that:

Takes two numbers a and b

Prints their sum, difference, product, and division

Use f-strings for all output
"""
def math_summary(a, b):
    print(f"Sum of {a} & {b} is {a + b}")
    print(f"Difference of {a} & {b} is {abs(a - b)}")
    print(f"Product of {a} & {b} is {a * b}")
    print(f"Division of {a} by {b} is {a / b:.2f}")

    print(" --- --- --- ")


"""
Challenge 04

Write a function format_name(first, last) that:

Capitalizes both first and last names

Returns a formatted string like: "Hello, John Doe!"
"""
def format_name(first, last):
    print(f"Hello, {first.upper()} {last.upper()}!")
    print(f"Hello, {first.lower()} {last.lower()}!")
    print(f"Hello, {first.title()} {last.title()}!")
    print(f"Hello, {first.capitalize()} {last.capitalize()}!")
    print(" --- --- --- ")


"""
Challenge 05

Write a one-liner list comprehension to:
Create a list of even numbers between 1 and 20 (inclusive)

[ expression  for item in iterable  if condition ]
"""
def challenge_05():
    even = [x for x in range(1, 21) if x % 2 == 0]
    print(even)
    print(" --- --- --- ")


### Ignition
if __name__ == "__main__":
    # challenge_01()
    # describe_input()
    # math_summary(5, 10)
    # format_name("john", "doe")
    challenge_05()
    