import string

for let in string.ascii_uppercase:
	file_name = f'{let}.txt'
	with open(file_name, 'w') as file:
		file.write(f'This is {let}.txt file')
	print(f'File {let} generated')


print('\nFiles gebenated succesfully')