# Tivoli Entrance prices: 8 years+, from 145DKK/ 3-7 years, 65DKK/ Under 3 years, 0DKK
age = int(input("How old are you? "))

if age >= 8:
    price = 145
else:
    if age >= 3:
        price = 65
    else:
        price = 0

print("You have to pay " + str(price) + " DKK.")