def no_dups(s):
    cache = {}

    word_list = s.split()
    new_string = ''

    for word in word_list:
        if word not in cache:
            cache[word] = word

    for key in cache:
        new_string = new_string + ' ' + key

    new_string.replace(" ", "")

    return new_string.strip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
