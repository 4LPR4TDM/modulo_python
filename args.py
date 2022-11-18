#! /usr/bin/python3

def conversion(year):
    nacimiento = 2022 - year
    print(f'Naciste en {nacimiento}')

def run():
    edad = int(input('Escribe tu edad\n'))
    conversion(edad)


if __name__ == '__main__':
    run()