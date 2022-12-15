# Without punctuation
def read(filename):
    with open(filename) as file:
        words = file.read().split()
        for i in range(len(words)):
            if words[i].startswith(('ADJECTIVE')):
                words[i] = input('Enter an adjective: ')
            if words[i].startswith(('NOUN')):
                words[i] = input('Enter a noun: ')
            if words[i].startswith(('ADVERB')):
                words[i] = input('Enter an adverb: ')
            if words[i].startswith(('VERB')):
                words[i] = input('Enter a verb: ')
        return ' '.join(words)

print(read('madlibs1.txt'))

