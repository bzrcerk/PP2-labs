def evens(n):
	for i in range(n+1):
		if i % 2 == 0:
			yield i

x = int(input("Enter number: "))

a = evens(x)

print(", ".join(map(str, a)))
