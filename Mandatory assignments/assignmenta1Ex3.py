# Tivoli Entrance prices: 8 years+, from 145DKK/ 3-7 years, 65DKK/ Under 3 years, 0DKK
age = int(input("How old are you? "))

if age < 8:
    if age < 3:
        price = 0
    else:
        price = 65
else:
    price = 145

print("You have to pay " + str(price) + "DKK.")








