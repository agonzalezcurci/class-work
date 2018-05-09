nospace = []

while True: 
	number = input("Enter a number: " )
	if number == 'done':
		break 
	try: 
		number = int(number)
	except:
		print('This is not a number try again')
		continue 
	print(number)
	nospace.append(number)	
print("Maximum: ", max(nospace))
print("Minimum: ", min(nospace))
