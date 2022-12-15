"""
You are in charge of a reservation system for a restaurant. The reservations
for a day are stored in a text file. Each line in the file stands for a reservation
and has the format: Name, Time, Status. Status is either CONFIRMED or
2
CANCELLED. Your task is to write a function show_reservations that takes
as argument a string filename, reads the file with the name filename and prints
all CONFIRMED reservations in order of the time. (You may assume that time
is an integer, the order for a reservation in the same slot is not important). You
may assume that all names are distinct."""

def show_reservations(filename):
    confirmed = {}
    with open(filename) as f:
        for line in f:
            name, time, status = line.split(", ")
            if status.strip() == "CONFIRMED":
                confirmed[name] = int(time)

    for name in sorted(confirmed, key=confirmed.get):
        print(f"{name}, {confirmed[name]}")

show_reservations("reservations1.txt")
