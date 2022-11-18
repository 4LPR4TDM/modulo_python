#!/usr/bin/python3

def run():
    try:
        ejemplo = int(input('Escribe un numero \n'))
        print(f'Escribiste {ejemplo}')
    except ValueError:
        print('Solo se aceptan numeros enteros')

    finally:
        print('Fin de este programa')


if __name__ == '__main__':
    run()