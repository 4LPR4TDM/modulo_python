#!/usr/bin/python3

def run():
	for contador in range(100):
		if contador %9 != 0:
			continue
		print(contador)


if __name__ == '__main__':
	run()
