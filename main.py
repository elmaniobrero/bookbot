#**aqui va todo lo del codigo main osea este es el proyecto**#
def main():
    print({number_words()}, "words found in the document")


def get_book_text():
    with open('books/frankenstein.txt') as f:
        book_contents = f.read()
        return book_contents

def number_words():
    texto = get_book_text()
    palabras = texto.split()
    contador = 0
    for p in palabras:
        contador = contador + 1
    return contador



main()