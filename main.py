#**aqui va todo lo del codigo main osea este es el proyecto**#

from stats import number_words
from stats import count_character
from stats import get_book_text
texto = get_book_text()
def main():
    print(number_words(), "words found in the document")
    print(count_character(texto))


main()
