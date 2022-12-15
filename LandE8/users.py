class User:


    def __init__(self, name, age, nationality):

        self.name = name
        self.age = age
        self.nationality = nationality


    def describe_user(self):

        print(f"{self.name} is a {self.age} year old {self.nationality}")

    def greet_user(self):

        print(f"Hi {self.name}!")

user1 = User("Angelina", "27", "Greek")
user2 = User("Klio", "26", "Greek")
user3 = User("Thor", "55", "Dane")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
