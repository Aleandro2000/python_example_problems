def count_words(word):
    word = word.lower()
    dictionary = {}
    count = 0
    list_words = word.split()
    for word in list_words:
        if word in dictionary:
            count +=1
            dictionary.update({word: count})
        else:
            count = 1
            dictionary.update({word: count})
    return dictionary
