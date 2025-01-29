class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def deposit(self):
		sum = int(input("Enter sum that you want to deposit: \n"))
		self.balance += sum
		print(f'Now your balance: {self.balance}')

	def withdraw(self):
		sum = int(input("Enter sum that you want to withdraw: \n"))
		if sum > self.balance:
			print(f'You don`t have enough money. Your balance: {self.balance}')
		else:
			self.balance -= sum
			print(f'Now your balance: {self.balance}')

person1 = Account("Max", 0)

while True:
	com = str(input("Enter the command: "))
	if com == 'q':
		break
	elif com == 'dep':
		person1.deposit()
	elif com == 'wtd':
		person1.withdraw()