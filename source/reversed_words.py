def reversed_words(word):
    list_words = word.split()
    for i in range(len(list_words)):
        list_words[i]=list_words[i][::-1]
    return list_words
    