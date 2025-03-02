import os

def lst(path):
	try:
		dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
		print(f'\nDirectories: ')
		for d in dirs:
			print(d)

		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
		print(f'\nFiles: ')
		for f in files:
			print(f)

		print(f'\nAll files and dirs: ')
		for i in os.listdir(path):
			print(i)
	except FileNotFoundError:
		print("The path does not exist")
	except PermissionError:
		print(f'Access denied')


path = input('Enter path:')
lst(path)