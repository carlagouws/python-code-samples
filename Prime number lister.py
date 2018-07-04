# ******************************************************************************************
# Description:
# Program asks the user for a number and prints out all primes numbers, including
# the input number, if prime
# EG:
'''
        Enter a number: 61
        Prime numbers: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
'''
# ******************************************************************************************

# Receive user input
maxNum = int(input('Enter a number: '))

def primeList(maxNumber):

    # Ensure number is prime
    # Keep repeating input prompt until the number is prime
    while maxNumber <= 1:
        print("That is not a prime number. Please input a larger number.")
        maxNumber = int(input('Enter a number: '))

    # Differentiate between a single and multiple numbers for output
    if maxNumber == 2:
        print("Prime number: ", end="")
    else:
        print("Prime numbers: ", end="")

    # Print 2 by default
    print(2, end=" ")

    # Calculate remaining numbers, if applicable
    for i in range(3, maxNumber+1):
        y = 0
        for x in range(2, i):
            num = i%x
            if num == 0:
                y += 1
        if y == 0:
            print(i, end=" ")

# Call function
primeList(maxNum)