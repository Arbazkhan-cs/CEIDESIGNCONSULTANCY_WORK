num = int(input("Enter a number: ")) # It will take integer input from the user and store it in num variable.
if num < 0: # if num is less than 0 then it will execute the next line.
    print(num, "is a negative number.") # If the number is negative then it will print this message.
elif num > 0: # if num is greater than 0 then it will execute the next line.
    print(num, "is a positive number.") # If the number is positive then it will print this message.
else: # If the number is not negative or positive then it will execute the next line.
    print(num, "is zero.") # If the number is zero then it will print this message.