# Write your code here :-)
name = input("What's your name? ")

char = ''

for char in name:
    if len(name) < 5:
        newName = input("This name is short!Try again! ")
        name = newName
    elif len(name) > 6:
        newlongname = input("This name is too long!Try again! ")
        name = newlongname
    else:
        print("Welcome " + name)





