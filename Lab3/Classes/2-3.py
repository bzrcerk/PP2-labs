class Shape:
	def __init__(self):
		self.length = 0
		self.width = 0
	def area(self):
		print(f'Now your area: {self.length * self.width}')
	
class Square(Shape):
	def __init__(self):
		super().__init__()
		self.length = int(input("Enter the size of Square: \n"))
		self.width = self.length

class Rectangle(Shape):
	def __init__(self):
		super().__init__()

		dimen = str(input('Enter length and width of your Rectangle: ')).split()
		
		self.length = int(dimen[0])
		self.width = int(dimen[1])
	


shape = Shape()
shape.area()

square = Square()
square.area()

rect = Rectangle()
rect.area()
