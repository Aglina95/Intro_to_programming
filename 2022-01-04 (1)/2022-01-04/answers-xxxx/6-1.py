def check_ta_count(rooms, tas):

    if rooms >= tas:
        return "Thank you very much for such a generous support."

    else:
        return "Unfortunately, I need more TAs to run the exercise sessions."


print(check_ta_count(11,11))
