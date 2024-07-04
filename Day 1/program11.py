def sum(num1:int, num2:int) -> int:
    return num1 + num2
num1 = int(input("Enter the first number: ")) # Get the first number from the user
num2 = int(input("Enter the second number: ")) # Get the second number from the user
print(f"{num1} + {num2} = {sum(num1, num2)}") # Call the sum function with the two numbers and print the result