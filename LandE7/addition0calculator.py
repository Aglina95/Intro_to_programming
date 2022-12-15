# Write your code here :-)
'''Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number'''

while True:

    try:
        num_1 = input("Enter a number ")
        if num_1 == "q":
            break
        num_1 = int(num_1)

        num_2 = input("Enter another number ")
        if num_2 == "q":
            break
        num_2 = int(num_2)

        addition = num_1 + num_2


        print(addition)

    except ValueError:

        msg = "I am sorry! This is not a number!"
        print(msg)
