# your code goes here
# Rules for documentation: Talk about the parameters, talk about
# what is returned.

class VaccineRecord:
    """
    A class to keep track of the vaccine treatment
    of a single patient.
    """

    def __init__(self, name, vaccine):
        """Creates a person with their name and
        the vaccine that is administered.
        """
        self.name = name
        self.vaccine = vaccine
        self.month = 0 # month of last vaccination
        self.year = 0 # year of last vaccination
        self.shots = 0 # total vaccination count

    def add_vaccination(self, month, year):
        """Add that person got a vaccine in
        certain month and year"""
        self.shots += 1
        # only update if it is a more recent date
        if (self.year < year) or (self.year == year and self.month < month):
            self.month = month
            self.year = year

    def vaccination_count(self):
        """Return the number of administered vaccinations."""
        return self.shots

    def print(self):
        print(f"{self.name} gets {self.vaccine} and got {self.shots} shots so far.")
        print(f"The last shot was administered at {self.month}/{self.year}.")

    def is_time_for_booster(self, month, year):
        if month + 12 * year - 7 >= self.month + 12 * self.year:
            return True
        return False

peter = VaccineRecord("Peter", "Pfizer")
katrine = VaccineRecord("Katrine", "Moderna")

print(peter.vaccination_count()) # 0
peter.add_vaccination(7, 2021)
peter.print()
peter.add_vaccination(4, 2021)
peter.print()
print(peter.vaccination_count())  # 1
print(peter.is_time_for_booster(12, 2021)) # False
print(peter.is_time_for_booster(1, 2022)) # False
print(peter.is_time_for_booster(2, 2022)) # True

peter.print()
