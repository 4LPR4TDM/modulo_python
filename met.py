#! /usr/bin/python3

def repla(name):
    nombre = name.replace('a','4')
    print(f'Hola {nombre}')


def run():
    name = str(input('Escribe tu AKA\n'))
    repla(name)

if __name__ == '__main__':
    run()