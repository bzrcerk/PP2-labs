def filt(nums):
	primes = []
	
	for i in nums:
		n = int(i)
		if n > 1:
			is_prime = True
			for j in range(2, n):
				if n % j == 0:
					is_prime = False
					break
			if is_prime: primes.append(n)

	print(primes) 
		

nums = input("Enter numbers separated by space: ").split(" ")

filt(nums)