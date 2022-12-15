# Write your code here :-)

"""Problem 3 (2 Points)
Marie and Leah each put together a file in which they rated certain movies with
a number from 1 to 10 (marie.txt and leah.txt). Each line in a file consists
of the name of the movie and the rating (from 1 to 10), split up by a “;”. Your
task is to print out all the movies that Marie and Leah both rated with 8 or
more.
Provide your solution in a file called 3.py.
Suggested Approach: Read each file into a dictionary. Go through one of the
dictionaries and check whether a key in there is also present in the other, and
both ratings are high enough. To avoid code duplication, you can define a
function read_file(filename) that reads a file and returns a dictionary.
"""

with open("marie.txt") as f:
    for line in f: # for each line do the following
        movie, rating = line.split(" ; ")
        if int(rating) >= 8:
            # I need to check the other file for this movie
            with open("leah.txt") as g: #
                for other_line in g:
                    other_movie, other_rating = other_line.split(" ; ")
                    if movie == other_movie and int(other_rating) >= 8:
                        print(movie)
