def break_words(stuff):
    """This function will break stuff into words"""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words"""
    return sorted(words)


def print_first_words(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints last word after popping it off"""
    word = words.pop(-1)
    print(word)


def sort_sentences(sentence):
    """This takes full sentences and returns sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def  print_first_and_last_sentence(sentence):
    """Prints first and last sentence."""
    words = break_words(sentence)
    print_first_words(words)
    print_last_word(words)


def  print_first_and_last_sentence(sentence):
    """Prints first and last sentence."""
    words = break_words(sentence)
    print_first_words(words)
    print_last_word(words)