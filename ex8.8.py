#using list and built in functions to calculate average

#create empty list 
numlist = list()

#create loop
while(True):
	inp = input("Enter Number: ")
	if inp == 'done':
		break
	value = float(inp)
	#append value to numlist 
	numlist.append(value)
#calculate average 
average = sum(numlist)/ len(numlist)
#print
print("Average: ", average)	
