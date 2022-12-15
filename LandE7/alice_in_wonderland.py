#this can work with multiple files i.e: filename = ['alice_in_wonderland', 'moby_dick.txt']
''' filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
 count_words(filename)'''

filename = 'alice_in_wonderland.txt'


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf8") as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
         # Count approximate number of words in the file.
         words = contents.split()
         num_words = len(words)
         print("The file " + filename + " has about " + str(num_words) + " words.")


count_words(filename)
