import os

def dell(path):

	if not os.path.exists(path):
		print("Path does not exist")
		return
	
	if not os.path.isfile(path):
		print("Path is not a file")
		return
	
	if not os.access(path, os.W_OK):
		print("File is not accesible")
		return
	
	os.remove(path)
	print("File deleted")


path = input("Enter path to the file: ")
dell(path)