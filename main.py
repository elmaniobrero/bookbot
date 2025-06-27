#**aqui va todo lo del codigo main osea este es el proyecto**#
def main():
    print(get_book_text())


def get_book_text():
    with open('books/frankenstein.txt') as f:
        book_contents = f.read()
        return book_contents

main()