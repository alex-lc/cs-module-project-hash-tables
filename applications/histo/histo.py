import re

with open('robin.txt') as f:
    words = f.read()


def histo(text):
    word_count = {}
    word_list = text.split()
    longest_word = ''

    for word in word_list:
        word = re.sub(r'[^\w\']', '', word)
        word = word.lower()
        if len(word) > len(longest_word):
            longest_word = word
        if word in word_count:
            word_count[word] += "#"
        else:
            if word != '':
                word_count[word] = "#"

    items = list(word_count.items())
    items.sort(key=lambda e: (-len(e[1]), e))
    word_count = dict(items)
    spaces = [' '] * (len(longest_word) + 1)
    spaces_str = " "
    spaces_str.join(spaces)

    for word in word_count:
        if word is not longest_word:
            print(
                f'{word}  {spaces_str.join(spaces)[:len(longest_word)-len(word)]}{word_count[word]}')
        else:
            print(f'{word}  {word_count[word]}')


histo(words)
