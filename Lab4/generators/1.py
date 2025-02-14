def square(n):
	for i in range(1, n+1):
		yield i**2

x = int(input("Enter the number: "))

a = square(x)

for i in a:
	print(i, end=' ')