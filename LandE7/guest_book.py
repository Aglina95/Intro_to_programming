# Write your code here :-)
'''Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file'''

filename = "guest_book.txt"
print("Enter quit if you have finished!")

while True:
    guest_name = input("What's your name? ")
    greet = "Greettings " + guest_name

    if guest_name == "quit":
        break
    else:
        print(greet)

    with open(filename, 'a') as file_object:
            file_object.write(guest_name + " was here!\n")


