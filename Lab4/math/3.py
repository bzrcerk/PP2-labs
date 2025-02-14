import math

n_s = int(input("Input number of sides: "))
l_s = int(input("Input the length of a side: "))


area = (n_s * l_s ** 2) / (4 * math.tan(math.pi / n_s))

print(f"The area of the polygon is: {round(area)}")