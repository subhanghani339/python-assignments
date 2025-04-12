# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

# CODE

def main():
    print("This Program add two numbers!")
    num1: str = (input("Enter First Number"))
    num1: int = int(num1)
    num2  : str = input("Enter second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("The total is " + str(total) + ".")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()