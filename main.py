#**aqui va todo lo del codigo main osea este es el proyecto**#
import sys
from stats import number_words
from stats import count_character
from stats import get_book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return
    
    syss = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at", syss)
    print("----------- Word Count ----------")
    print("Found",number_words(syss),"total words")
    print("--------- Character Count -------")
    texto = get_book_text()
    chars = count_character(texto)
    
    for item in chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
   


main()
