# Write your code here :-)
class User:


    def __init__(self, name, age, nationality):

        self.name = name
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0


    def describe_user(self):

        print(f"{self.name} is a {self.age} year old {self.nationality}")

    def greet_user(self):

        print(f"Hi {self.name}!")

    def read_login_attempts(self):
        print(f"The user tried to log in {self.login_attempts} times")

    def reset_login_attempts(self):
         if self.login_attempts > 0:
            self.login_attempts = 0
            print("Login attempts were reset")
         else:
            print("You can't roll back an odometer!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        #print(login_attempts)

class Admin(User):

    def __init__(self, name, age, nationality):
        super().__init__(name, age, nationality)
        self.privileges = []

    def show_privileges(self):
        print("You can:")
        for privilege in self.privileges:
            print(privilege)


user1 = Admin("Angelina", 27, "Greek")

user1.describe_user()

user1.privileges = [
    'reset passwords',
    'moderate discussions',
    'suspend accounts',
    ]

user1.show_privileges()
