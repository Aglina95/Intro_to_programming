# Write your code here :-)
toppings = ""


print("Enter 'quit' to exit the program")

while True:

    topping = input("Which topping should be put on your pizza? ")

    if topping == "quit":
        print("Expect your " + toppings + " pizza delivered in 10 minutes.")

    else:
        toppings = toppings + " " + topping
        print("Excelent choice! Your pizza now contains " + toppings)
        continue

    break

