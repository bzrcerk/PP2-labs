class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def show(self):
		print(f'Your point at ({self.x},{self.y}) coordinates')

	def move(self, x, y):
		self.x = x
		self.y = y

	def dist(self, other_point):
		dis = ((other_point.x - self.x)**2 + (other_point.y - self.y)**2)**(0.5)
		print(f'Distance between two points is {round(dis, 2)}')

point1 = Point(-2, -2)
point2 = Point(2, 6)

point1.dist(point2)