# Write your code here :-)
#print(3+3) #expression: an expression is made of values and operators.

#Actions/ Functions

#i.e print() is a function. If you call print with a number, it converts it to a string.
# str(6) -> "6"

#Data types: strings = "3 + 3", floats = 1, 2, ints = 6

#Operators: "N" * 4 = NNNN
#print("A" + 3) = Type Error
#print("A"+"B") = concatenation. AB

# This program says hello and asks for my name.
#print('Hello, world!')
#print('What is your name?') # ask for their name
#myName = input() #Input returns strings
#print('It is good to meet you, ' + myName)
#print('The length of your name is:')
#print(len(myName)) #len = length: how long the string is
#print('What is your age?') # ask for their age
#myAge = input()
#print('You will be ' + str(int(myAge) + 1) + ' in a year.')

print("Hello, World")
myName = input("What is your name? ")
print("It is goot to meet you, " + myName)
print("The length of your name is " + str(len(myName)))
myAge = input("What is your age?")
myAge = int(myAge)
myAge = myAge + 1
myAge = str(myAge)
myAge = myName
myName = "Emma"
print("You will be " + myAge + " in a year.")
print("And your name is still " + myName)

