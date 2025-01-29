import math
def vol(rad):
	res = (4/3) * (math.pi * rad**3)
	print(round(res))

x = int(input("Enter radius: "))

vol(x)