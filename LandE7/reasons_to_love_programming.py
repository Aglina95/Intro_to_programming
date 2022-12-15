# Write your code here :-)
'''Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.'''

filename = "reasons_to_love_programming.txt"
print("Enter quit if you have finished!")

while True:
    reason_to_like_programming = input("Why do you like programming? ")

    if reason_to_like_programming == "quit":
        break

    with open(filename, 'a') as file_object:
            file_object.write(f'{reason_to_like_programming}\n')
