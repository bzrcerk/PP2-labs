import os

def check(path):
	print(f"Checking path: {path}")

	if os.path.exists(path):
		print("\nFollowing path exists")
	else:
		print("ERROR Path does not exist")
		return
	
	pth = os.scandir(path)

	for entry in pth:
		if os.path.isdir(entry.path):
			print(f"\nDirectory name: {entry.name}")
			print(f"Directory: {(entry.path).removesuffix(entry.name)}")
		else:
			print(f"\nFile name: {entry.name}")
			print(f"Directory: {(entry.path).removesuffix(entry.name)}")


path = input("Enter path: ")
check(path)
	