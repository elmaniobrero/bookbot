

def get_book_text(syss):
    with open(syss,"r", encoding="utf-8") as f:
        book_contents = f.read()
        return book_contents

def number_words(syss):
    texto = get_book_text(syss)
    palabras = texto.split()
    contador = 0
    for p in palabras:
        contador = contador + 1
    return contador

def count_character(texto):
   
    abc= {}
    
    for le in texto:
        letrasm = le.lower()
        if(letrasm in abc ):
            abc[letrasm] = abc[letrasm] + 1 
        else:
            abc[letrasm] = 1
    
    lista = [{"char": char, "num": count} for char, count in abc.items()]
    lista.sort(key=lambda x: x["num"], reverse=True)
    
    return lista


    

