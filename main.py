#**aqui va todo lo del codigo main osea este es el proyecto**#

from stats import number_words
from stats import count_character
from stats import get_book_text

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found",number_words(),"total words")
    print("--------- Character Count -------")
    print(count_character(get_book_text()))
    print("============= END ===============")



main()
