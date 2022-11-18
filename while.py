#! /usr/bin/python3
def run():
    id = int(input('Escribe el id de usario\n'))
    while id <= 200000:
        print(f'Hackeando al usuario con ID = {id}')
        id = id + 1


if __name__ == '__main__':
    run()