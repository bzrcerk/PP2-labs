def squares(a, b):
	for i in range(a, b+1):
		yield i**2

a = int(input("Enter start: "))
b = int(input("Enter end: "))

x = squares(a, b)

for i in x:
	print(i, end=" ")