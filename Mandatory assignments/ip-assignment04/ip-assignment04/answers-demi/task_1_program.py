# This is the program for task 1
# Make sure that your answers are provided in the file 1.txt!
def find_longest_word(dictionary):

    longest_word = dictionary[0]
    for word in dictionary:
        if len(word) > len(longest_word):
            longest_word = word

    return len(longest_word)

def find_word_with_most_z(dictionary):
    word_with_most_z = dictionary[0]
    for word in dictionary:
        if word.count('z') > word_with_most_z.count('z'):
            word_with_most_z = word

    return word_with_most_z

# read dictionary.txt line-by-line into a list of strings.
content = open('dictionary.txt').readlines()

content_without_new_lines = []
for line in content:
    content_without_new_lines.append(line.replace("\n",""))


print("Longest word:", find_longest_word(content_without_new_lines))
print("Word with most z:", find_word_with_most_z(content_without_new_lines))
