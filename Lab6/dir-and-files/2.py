import os

# W_OK - writable
# R_OK - readable
# X_OK - execurable

def check(path):
	print(f"Checking access for {path}\n")

	if os.path.exists(path):
		print("Path exists!")
	else:
		print("ERROR file does not exist")
		return
	
	if os.path.isfile(path):
		print("Path is file.")
	elif os.path.isdir(path):
		print("Path is directory.")

	if os.access(path, os.W_OK):
		print("Path is Writable!")
	else:
		print("ERROR Path is not Wirteble")

	if os.access(path, os.R_OK):
		print("Path is Readable!")
	else:
		print("ERROR Path is not Readable")

	if os.access(path, os.X_OK):
		print("Path is Executable!")
	else:
		print("ERROR Path is not Executable")

path = input("Enter the path: ")
check(path)