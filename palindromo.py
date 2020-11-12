def run():
    palabra = str(input("Escribe un palabra: ")).lower().replace(' ', '')
    if palabra[::] == palabra[::-1]:
        print('Es palíndromo')
        run()
    else:
        print('No es palíndromo')
        run()

if __name__ == '__main__':
    run()