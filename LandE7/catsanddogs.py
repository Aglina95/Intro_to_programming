# Write your code here :-)
list_of_files = ['cats.txt', 'dogs.txt']

def count_words(filename):
    """word counter"""
    try:
        with open(filename) as file_object:
            lines = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
         # Count approximate number of words in the file.
         words = lines.split()
         num_words = len(words)
         print("The file " + filename + " has about " + str(num_words) + " words.")



for file in list_of_files:
    count_words(file)
