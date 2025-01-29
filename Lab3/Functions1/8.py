def spy(nums):
	for i in range(len(nums)-2):
		if nums[i] == '0' and nums[i+1] == '0' and nums[i+2] == '7':
			print(True)
			return
	print(False)
	return

x = list(input())

spy(x)