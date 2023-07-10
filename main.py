from source.largest_unique_number import largest_unique_number
from source.remove_duplicates import remove_duplicates
from source.reversed_words import reversed_words
from source.find_missing_number import find_missing_number
from source.is_anagram import is_anagram
from source.validate_palindrome import validate_palindrome
from source.prime_factors import prime_factors
from source.count_words import count_words
from source.matrix_transpose import matrix_transpose
from source.binary_search import binary_search

def main():
    print("Problems list:\n\n")
    print("1->largest_unique_number")
    print("2->remove_duplicates")
    print("3->reverse_words")
    print("4->find_missing_number")
    print("5->is_anagram")
    print("6->validate_palindrome")
    print("7->prime_factors")
    print("8->count_words")
    print("9->matrix_transpose")
    print("10->binary_search")
    print("11->EXIT")
    
    option = input("Option: ")
    while option != "11":
        if option == "1":
            number_list = list(map(int,input("Numbers input: ").split(' ')))
            print(largest_unique_number(number_list))
        elif option == "2":
            array_list = list(map(str,input("List input: ").split(' ')))
            print(remove_duplicates(array_list))
        elif option == "3":
            words = input("Words: ")
            print(reversed_words(words))
        elif option == "4":
            missing_muber = list(map(int,input("List of integers from 1 to N (inclusive) with one number missing: ").split(' ')))
            print(find_missing_number(missing_muber))
        elif option == "5":
            word1 = input("Word 1: ")
            word2 = input("Word 1: ")
            print(is_anagram(word1, word2))
        elif option == "6":
            string = input("String for palindrome validation: ")
            print(validate_palindrome(string))
        elif option == "7":
            number = int(input("Number input: "))
            print(prime_factors(number))
        elif option == "8":
            words = input("Words: ")
            print(count_words(words))
        elif option == "9":
            R = int(input("Enter the number of rows:"))
            C = int(input("Enter the number of columns:"))
            matrix = []
            print("Enter the entries rowwise:")
            for i in range(R):
                a =[]
                for j in range(C):
                     a.append(int(input()))
                matrix.append(a)
            print(matrix_transpose(matrix))
        elif option == "10":
            array = list(map(int,input("Array input for bynary search: ").split(' ')))
            number = int(input("Number input for inding in array using bynary search: "))
            print(binary_search(array, 0, len(array)-1, number))
        option = input("Option: ")

if __name__=="__main__":
    main()