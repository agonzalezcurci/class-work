count = 0
total = 0

while True: 
	number = input("Enter a number" )
	if number == 'done':
		break 
	print(number)
	count = count + 1
	total = total + int(number)
	ave = total/count	
print(count,total,ave)
