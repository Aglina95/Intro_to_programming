def remove_characters(line, characters_to_remove):
    new_line = []
    for character in line:
        if character in characters_to_remove:
            continue
        else:
            new_line.append(character)
    
    return "".join(new_line)

# lists

bee_movie_script_lines = []

with open("./bee-movie.txt", "r") as bee_movie_file:
    bee_movie_script_lines = bee_movie_file.readlines()

bee_movie_script_lines_without_newlines = []
for line in bee_movie_script_lines:
    bee_movie_script_lines_without_newlines.append(line.replace("\n",""))

characters_to_remove = ["-",".",",","!","?"]

bee_movie_script_lines_cleaned = []
for line in bee_movie_script_lines_without_newlines:
    bee_movie_script_lines_cleaned.append(remove_characters(line, characters_to_remove))

words = []
for line in bee_movie_script_lines_cleaned:
    for word in line.split(" "):
        if len(word) == 0:
            continue

        words.append(word)

words_lowercase = []
for word in words:
    words_lowercase.append(word.lower())

# dictionaries

# {"of": 3, "to": 15, "car": 1}
word_count = {}

for word in words_lowercase:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] = word_count[word] + 1

word_counts_list = []
for word,count in word_count.items():
    word_counts_list.append((word, count))

# x => x[1]
word_counts_list.sort(key = lambda element: element[1], reverse = True)

top_5_word_count_tuples = word_counts_list[0:5]

with open("./word_counts.txt", "w") as word_count_file:
    for (word,count) in word_counts_list:
        word_count_file.write("Word: {0} Count: {1} \n".format(word, count))

pass




