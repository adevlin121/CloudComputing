sum = 0
counter = 0
for counter in range(0, 1000):
	counter = counter + 1
	if counter % 3 == 0:
		sum = sum + counter
	elif counter % 5 ==0:
		sum = sum + counter
print sum
