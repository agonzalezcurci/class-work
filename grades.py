try: 
	grade = float(input('Enter Grade'))
	if grade < 1:
		if grade >= 0.9: 
			print('A')
		elif grade >= 0.8:
			print('B')
		elif grade >= 0.7:
			print('C')
		elif grade >= 0.6:
			print('D')
		elif grade >= 0.5:
			print('F')
	else: 
		print('Bad Score')
except: 
	print('Bad Score')
	 
	