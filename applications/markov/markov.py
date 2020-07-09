import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words


def gobbledegook(text):
    words_list = text.split()
    cache = {}

    for i in range(len(words_list)-1):
        if words_list[i] in cache:
            cache[words_list[i]].append(words_list[i+1])
        else:
            cache[words_list[i]] = [words_list[i+1]]
    cache[words_list[-1]] = []
    return cache


sentence = "Cats and dogs and birds and fish dogs birds?"
# print(gobbledegook(sentence))

# TODO: construct 5 random sentences


def make_random_sentences(text):
    cache = gobbledegook(text)
    random_word = random.choice(text.split())

    stop_conditions = ['.', '?', '!', '."', '?"', '!"']

    current_words = cache[random_word]
    curr = random.choice(current_words)
    sentence = random_word

    while curr[-1] not in stop_conditions and curr[-2:] + curr[-1] not in stop_conditions and len(cache[curr]) > 1:
        if cache[curr] != [] and cache[curr] != None:
            sentence = sentence + " " + curr
            curr = random.choice(cache[curr])
        else:
            curr = random.choice(current_words)

    sentence += " " + curr
    print(sentence)


make_random_sentences(words)
make_random_sentences(words)
make_random_sentences(words)
make_random_sentences(words)
make_random_sentences(words)
