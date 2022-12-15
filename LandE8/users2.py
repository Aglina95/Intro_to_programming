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

user1 = User("Angelina", "27", "Greek")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.read_login_attempts()



