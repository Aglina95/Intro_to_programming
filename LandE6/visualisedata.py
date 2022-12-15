# Write your code here :-)

key_value = 0

def print_data(dictionary):
    for year, inhab in dictionary.items():
        print(year, "∎" * (inhab // 100000), inhab)

cph_over_years = {
    1880: 266466,
    1890: 367262,
    1901: 468936,
    1911: 584089,
    1921: 700610,
    1930: 771168,
    1940: 890130,
    1950: 974901,
    1960: 923974,
    1970: 802391,
    1975: 729357,
    1976: 1292647,
    1981: 1381882,
    1985: 1358540,
    1990: 1337114,
    1995: 1353333,
    1999: 1069813,
    2000: 1075851,
    2007: 1145804,
    2009: 1167569,
    2011: 1199224,
    2012: 1213882,
    2017: 1295686,
}

print_data(cph_over_years)


