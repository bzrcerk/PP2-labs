file_name = 'test_for_4.txt'

lst = ['1', '2', '3', '4']

with open(file_name, 'w') as file:
	for it in lst:
		file.writelines(it + '\n')