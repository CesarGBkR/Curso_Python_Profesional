# Podemos asignar el tipo esperado en el argumento de una función colo cando ":" al terminar el nombre de la variable
# seguido de el tipo al que la limitarémos.
# También podemos agregar "->" después de los parentesis para asignar el tipo esperado de salida.

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome(100))

if __name__ == '__main__':
    run()