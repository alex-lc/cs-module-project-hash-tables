import re


def word_count(text):
    word_count = {}
    word_list = text.split()
    for word in word_list:
        word = re.sub(r'[^\w\']', '', word)
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            if word != '':
                word_count[word] = 1
    return word_count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
