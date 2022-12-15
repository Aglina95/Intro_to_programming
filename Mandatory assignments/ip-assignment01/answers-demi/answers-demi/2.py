minutes = int(input("How many minutes do you shower per day? "))

water_day = 8 * minutes
#print(water_day)
water_year = water_day * 365
#print(water_year)

print("You spend " + str(water_day) + " liters of water per day showering.")
print("You spend " + str(water_year) + " liters of water per year showering.")

if water_day > 80:
    print("You spend too much water!")