# YOUR CODE GOES HERE
import datetime
class DataBase:
    def __init__(self, messages_file, meta_data_file):
        self.messages_file = messages_file
        self.meta_data_file = meta_data_file

        self.messages = self.read_file(messages_file)
        self.meta_data = self.read_file(meta_data_file)


    def read_file(self, filename):
        lines_without_newlines = []
        with open(filename, "r", encoding="utf-8") as file_object:
            for line in file_object:
                lines_without_newlines.append(line.replace("\n",""))

            return lines_without_newlines

    def show_by_author(self, name):
        for meta_data_line, message_line in zip(self.meta_data, self.messages):
            meta_data_line_split = meta_data_line.split(" ")
            author_name = meta_data_line_split[3]

            if author_name == name:
                print(message_line)


    def show_date_range(self, from_year, from_month, from_day, to_year, to_month, to_day):
        for meta_data_line, message_line in zip(self.meta_data, self.messages):
            meta_data_line_split = meta_data_line.split(" ")
            year = int(meta_data_line_split[0])
            month = int(meta_data_line_split[1])
            day = int(meta_data_line_split[2])
            date = datetime.datetime(year, month, day)

            from_date = datetime.datetime(from_year, from_month, from_day)
            to_date = datetime.datetime(to_year, to_month, to_day)

            if date >= from_date and date <= to_date:
                print(message_line)



    def show_by_match(self, message):
        for line in self.messages:
            if message in line:
                print(line)


db = DataBase('../8/message.txt', '../8/meta.txt')

#db.show_by_author("Henrik")

#db.show_by_match("Har")

db.show_date_range(1999, 12, 3, 2020, 12, 8)
