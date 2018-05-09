hours = int(input('Enter Hours'))
rate = input('Enter Pay')
if hours > 40:
	regpay = hours * float(rate)
	overtime = (0.5 * float(rate)) * (hours - 40)
	pay = regpay + overtime
	
else:
	pay = hours * float(rate)
	
print(pay)