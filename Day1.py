# Program - 1
print("Program - 1")
print("Hello, World!") # It will print the text which is written inside the double quotes.

# Program - 2
print("\nProgram - 2")
name = "Arbaz khan" # name is a variable which stores name of the person.
age = 19 # age is a variable which stores age of the person.
hobby = "Programming" # hobby is a variable which stores favorite hobby of the person.
print("My name is " + name + ", I am " + str(age) + " years old and I love " + hobby) # It will print all the variables

# program - 3 explaining all the lines in the code

# Program - 4
print("\nProgram - 4")
num = int(input("Enter a number: ")) # It will take integer input from the user and store it in num variable.
if num < 0: # if num is less than 0 then it will execute the next line.
    print(num, "is a negative number.") # If the number is negative then it will print this message.
elif num > 0: # if num is greater than 0 then it will execute the next line.
    print(num, "is a positive number.") # If the number is positive then it will print this message.
else: # If the number is not negative or positive then it will execute the next line.
    print(num, "is zero.") # If the number is zero then it will print this message.

# Program - 5
print("\nProgram - 5")
year = int(input("Enter a year: ")) # Get user input

# Check if the year is a leap year
if (year % 4 == 0): # If the year is divisible by 4
    if (year % 100 == 0): # If the year is divisible by 100
        if (year % 400 == 0): # If the year is divisible by 400
            print(f"{year} is a leap year.") # Then print it is a leap year
        else: # If the year is not divisible by 400
            print(f"{year} is not a leap year.") # Then print it is not a leap year 
    else: # If the year is not divisible by 100
        print(f"{year} is a leap year.") # Then print it is a leap year
else:# If the year is not divisible by 4
    print(f"{year} is not a leap year.") # Then print it is not a leap year

# Program - 6
print("\nProgram - 6")
for i in range(1, 11): # Loop through numbers from 1 to 10
    print(i, end=" ") # Print the number and a space

# Program - 7
print("\n\nProgram - 7")
num = int(input("Enter a number: ")) # Get user input
for i in range(1, 11): # Loop through numbers from 1 to 10
    print(f"{num} x {i} = {num * i}") # Print the multiplication table

# Program - 8
print("\n\nProgram - 8")
for i in range(1, 11): # Loop through numbers from 1 to 10
    if i % 3 == 0: # Check if the number is divisible by 3
        continue # Skip the rest of the code and continue with the next iteration
    print(i, end=" ") # Print the number and a space

# Program - 9
print("\n\nProgram - 9")
i = 1 # Initialize i to 1
while True: # Infinite loop
    print(i, end=" ") # Print the value of i
    i += 1 # Increment i by 1
    if i > 5: # Check if i is greater than 5
        break # Exit the loop

# Program - 10
print("\n\nProgram - 10")
def greet(name:str) -> str: # Define a function called greet that takes a parameter called name
    print(f"Hello, {name}!") # Print a greeting message with the name

greet("Alice") # Call the greet function with the argument "Alice"

# Program - 11
print("\nProgram - 11")
def sum(num1:int, num2:int) -> int:
    return num1 + num2
num1 = int(input("Enter the first number: ")) # Get the first number from the user
num2 = int(input("Enter the second number: ")) # Get the second number from the user
print(f"{num1} + {num2} = {sum(num1, num2)}") # Call the sum function with the two numbers and print the result