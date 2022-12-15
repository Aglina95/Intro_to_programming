# Write your code here :-)
age = int(input('How old are you?: '))

if age >= 65:
    print("The person is an elder")
else:
    if age >= 20 and age < 65:
        print("The person is an adult")
    elif age >= 13 and age < 20:
        print("The person is a teenager")
    elif age >= 4 and age < 13:
        print("The person is a kid")
    elif age >= 2 and age < 4:
        print("The person is a toddler")
    else:
        print("The person is a baby")



