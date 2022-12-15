def assign_tas(rooms, tas):
    tas_range = range(1, tas + 1)

    for ta in tas_range:
        """if ta > rooms:
            room_new = rooms
        else:
            room_new = ta"""

        room_new = min(ta, rooms)

        print("TA " + str(ta) + " goes to room " + str(room_new) )

    #print(f'TA {tas} goes to room {room}')

assign_tas(3, 12)


