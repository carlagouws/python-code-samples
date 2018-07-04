# ******************************************************************************************
# Description:
# The program sorts a list of numbers in ascending order
# EG:
'''
        Numbers to sort:
        [61, 28, 42, 76, 11, 93, 7, 81, 3, 53]
        Sorted numbers:
        [3, 7, 11, 28, 42, 53, 61, 76, 81, 93]
'''
# ******************************************************************************************

# Defines the list of numbers to sort and displays
listNum = [61, 28, 42, 76, 11, 93, 7, 81, 3, 53]
print("Numbers to sort:")
print(listNum)
print()

length = len(listNum)

listNum = listNum + [0]

x = 0

# 2 loops are required
# The outer loop chooses chooses a number to evaluate
# The inter loop compares the number to the next number and swops them if necessary
for j in range(length+1):
    for i in range(0, length):
        if listNum[i] > listNum[i+1]:
            x = listNum[i+1]
            listNum[i+1] = listNum[i]
            listNum[i] = x
    j += 1

# Defines the sorted list of numbers and displays
listNum = listNum[1:length+1]
print("Sorted numbers:")
print(listNum)