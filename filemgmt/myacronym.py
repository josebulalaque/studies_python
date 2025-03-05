
lookup = input('Please input the Acronym you want to lookup:\n')

# with keyword makes sure the File is properly closed when the file operations 
# are done even if an exception is raised
# it is a shortcut for block below
# file = open("myinput.txt")
# try:
#     pass
# finally
#     file.close()

found = False

with open("myinput.txt") as file:
    #result = file.readlines() # as shortcut, you can just loop from the file below and comment this out
    for i in file:
        if lookup in i: #checks if a string is a substring of another string
            print(i)
            found = True

if not found:
    print("The Acronym does not exist")

# readlines() method returns a list of Strings of all of the lines in the file
# you can loop from readlines() output to print the contents

# readline() methos returns the next line of the file as String
# read() method returns the whole file as String, or it will return the specified number of bytes


