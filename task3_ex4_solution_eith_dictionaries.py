# Write your code here :-)
#Task 3 Exercise 4 Solution with dictionaries:

def read_file(filename):
    movie_dict = {}
    with open(filename) as f:
        for line in f: # for each line do the following
            movie, rating = line.split(" ; ")
            movie = movie.strip()
            rating = int(rating)
            movie_dict[movie] = rating
    return movie_dict

marie_dict = read_file("marie.txt")
leah_dict = read_file("leah.txt")

for movie, rating in marie_dict.items():
    if rating >= 8 and movie in leah_dict and leah_dict[movie] >= 8:# leah gave it also an 8+:
    #if rating >= 8 and leah_dict.get(movie, 0) >= 8: # Alternative solution
        print(movie)

#the running time of this solution is O(N^2)

#other solution
def read_file(filename):
    l = []
    with open(filename, encoding='utf8') as f:
        for line in f:
            l.append(line.split(" ; "))
    return l


leah_list = read_file("leah.txt")
marie_list = read_file("marie.txt")

for movie, rating in marie_list:
    if int(rating) < 8: # skip movies that have rating below 8
        continue
    for other_movie, other_rating in leah_list:
        if movie == other_movie and int(other_rating) >= 8:
            print(movie)

#the running time of this solution is O(N^2)
