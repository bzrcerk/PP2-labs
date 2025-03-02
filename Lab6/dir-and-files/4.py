file_name = 'test.txt'

with open(file_name, 'r') as file:
	print(len(file.readlines()))