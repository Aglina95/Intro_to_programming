# Write your code here :-)


def collatz(number):

    if number % 2 == 0:
        divide_even = number // 2
        print(divide_even)
        return divide_even
    elif number % 2 == 1:
        divide_odd = 3 * number + 1
        print(divide_odd)
        return divide_odd

try:
    n = int(input("Type a number: "))

    while n != 1:
        n = collatz(int(n))

except ValueError:
    print("You must enter a number")




