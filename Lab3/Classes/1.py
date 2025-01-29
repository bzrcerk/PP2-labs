class My_Str:
	
	def getString(self):
		self.string = str(input("Enter your string: \n"))

	def printString(self):
		print(self.string.upper())

str1 = My_Str()

str1.getString()
str1.printString()