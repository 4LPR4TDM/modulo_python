#! /usr/bin/python3
def clave(usuario):
    clave_correcta = '123456'

    if usuario == clave_correcta:
        print('Has activado el producto')
    elif usuario == '1584':
        print('has activado el producto 2')
    else:
        print('Clave incorrecta')

def run():
    clave_usuario = str(input('Escribe la clave del producto \n'))
    clave(clave_usuario)

if __name__ == '__main__':
    run()