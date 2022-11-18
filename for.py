#! /usr/bin/python3

def exist():
    print('Respuesta incorrecta solo:')

    for i in range(1001):
        print(f'Existe el usuario {i}')
def run():
    respuesta = int(input('Cuantos usuarios del sistema existen? \n'))
    
    if respuesta == 1000:
        print('Respueast correcta')

    else:
        exist()

if __name__ == '__main__':
    run()