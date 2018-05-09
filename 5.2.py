largest = 0
smallest = 0

while True: 
	number = input("Enter a number" )
	if number == 'done':
		break 
	print(number)
	if number < smallest:
		smallest = number
    if number > largest:
    	largest = number	
print('Smallest:', smallest)	
print('Largest:', largest)

