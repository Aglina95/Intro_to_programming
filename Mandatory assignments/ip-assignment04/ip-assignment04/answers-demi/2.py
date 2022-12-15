def read_reservation(filename):
    # YOUR CODE HERE
    list_of_confirmed = []
    file_object = open(filename).readlines()
    for line in file_object:
        if "CONFIRMED" in line:
            line_split = line.split(",")
            time_int = int(line_split[1])
            name_time = [line_split[0], time_int]
            list_of_confirmed.append(name_time)

    def get_second_element(sub_list):
        int_element = sub_list[1]

        return int_element

    sorted_list = sorted(list_of_confirmed, key=get_second_element, reverse=True)
    return sorted_list


def show_reservations(filename):
    list_of_reservations = read_reservation(filename)
    for reservation in list_of_reservations:
        reservation = reservation[0] + ", " + str(reservation[1])
        print(reservation)


print("Reservations from first file:")
show_reservations("reservations1.txt")
print()
print("Reservations from second file:")
show_reservations("reservations2.txt")
