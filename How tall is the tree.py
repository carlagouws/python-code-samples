# ******************************************************************************************
# Description:
# Program asks the user how tall the tree is
# User inputs the height of the tree in number of rows, e.g. "9" produces a height of 9 rows
'''
        How tall is the tree : 5
            #
           ###
          #####
         #######
        #########
            #
'''
# ******************************************************************************************

# Variables:
# Number of rows (rows)
# Number of iterations (i)
# Number of hashtags = i*2 - 1
# Number of spaces = rows - i

# Receive user input and make integer
rows = int(input('How tall is the tree?: '))

# Body of pine tree
i = 1
while i <= rows:

    # Insert required amount of spaces
    NumSpaces = rows - i
    for spaces in range(NumSpaces):
        print(" ", end = "")

    # Insert required amount of hashtags
    NumHashtags = i*2 - 1
    for hashtags in range(NumHashtags):
        print("#", end = "")

    # Enter
    print()

    # Increment iteration
    i += 1

# Base of pine tree
BaseSpaces = rows - 1
for spaces in range(BaseSpaces):
    print(" ", end="")
print("#")