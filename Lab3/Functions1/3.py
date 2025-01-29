def solve(numheads, numlegs):
	a1, b1, a2, b2 = 1, 1, 2, 4
	y = abs(-(numlegs - 4 * numheads) / 2)
	x = numheads - y
	print(f' Amount of rabbits: {int(x)} \n Amont of chickens: {int(y)}')

x = int(input())
y = int(input())

solve(x,y)