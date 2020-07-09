import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words


def gobbledegook(text):
    words_list = text.split()
    cache = {}

    for word in range(len(words_list)):
        if words_list[word] not in cache:
            cache[words_list[word]] = [words_list[word], words_list[word + 1]]
    
    print(cache)

# TODO: construct 5 random sentences
# Your code here


gobbledegook(words)
