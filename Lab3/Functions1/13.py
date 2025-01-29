import random

rand = random.randint(1, 20)

name = str(input("Hello! What is your name?\n"))

cnt = 0

while True:
	if cnt == 0:
		print(f'Well, {name}, I am thinking of a number between 1 and 20. \nTake guess.')
	res = int(input())
	if res > rand:
		print(f'Your guess is too high. \nTake a guess.')
	elif res < rand:
		print(f'Your guess is too low. \nTake a guess.')
	else:
		print(f'Good job, KBTU! You guessed my number in {cnt + 1} guesses!')
		break
	cnt+=1
