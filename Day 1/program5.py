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