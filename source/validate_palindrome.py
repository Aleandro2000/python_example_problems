from re import sub

def validate_palindrome(word):
    word_to_be_check = sub(r'[^\w+]', '', word)
    return word_to_be_check[::-1] == word_to_be_check