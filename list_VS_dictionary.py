# Benchmarking List VS Dictionary
Constructing the input took 0.01 seconds.
Solving the task using the dictionary took 0.00 seconds.
Solving the task using the list took 6.26 seconds.
from timeit import default_timer

N = 10000

marie_dict = {}
leah_dict = {}
marie_list = []
leah_list = []

# make an artificial list of N movies called 0, ..., N - 1,
# each rated by both 10.
start = default_timer()
for i in range(N):
    marie_dict[i] = 10
    leah_dict[i] = 10
    marie_list.append([i, 10])
    leah_list.append([i, 10])

print(f"Constructing the input took {(default_timer() - start):.2f} seconds.")

cnt_dict = 0
cnt_list = 0

# search through dictionary O(N)

start = default_timer()
for movie, rating in marie_dict.items():
    if rating >= 8 and movie in leah_dict and leah_dict[movie] >= 8:# leah gave it also an 8+:
        cnt_dict += 1

print(f"Solving the task using the dictionary took {(default_timer() - start):.2f} seconds.")

# search through lists O(N^2)

for movie, rating in marie_list:
    if int(rating) < 8: # skip movies that have rating below 8
        continue
    for other_movie, other_rating in leah_list:
        if movie == other_movie and int(other_rating) >= 8:
            cnt_list += 1

print(f"Solving the task using the list took {(default_timer() - start):.2f} seconds.")

assert cnt_dict == N
assert cnt_list == N
