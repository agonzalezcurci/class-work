largest = 0
smallest = 0

while True: 
	x = input("Enter a number" )
	if x == 'done':
		break
	try: 
		number = int(x)
	except:
		print('This is not a number try again')
		continue 
	print(x)
if number < smallest:
	smallest = number
if int(number) > largest:
    largest = number	
print('Smallest:', smallest)	
print('Largest:', largest)