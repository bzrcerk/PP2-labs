nums = [1,2,3,4,5,5,6,7,8,9,10,22,93,91,1415,17,19]
cmp = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x)))

primes = list(filter(cmp, nums))

print(primes)