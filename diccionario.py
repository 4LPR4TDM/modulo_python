#!/usr/bin/python3

def run():
	diccionario_uno = {
		'llave 1': 66,
		'llave 2': 67,
		'llave 3': 68
	}

	# print(diccionario_uno['llave 1'])


	for i in diccionario_uno.keys():
		print(i)

	for i in diccionario_uno.values():
		print(i)

	
	for i in diccionario_uno.items():
		print(i)

	

if __name__ == '__main__':
	run()
