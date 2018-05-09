# create composite key to map last-name first-name pairs with phone numbers 
# expression in brackets is tuple, we can use tuple assignment in a for loop to traverse a dictionary  
directory[last,first] = number 

for first, last in dictionary:
	directory(first, last, directory[last,first])

# this loop traverse keys in directory which are tuples, assigning elements of 
#each tuple to last and first and prints name and corresponding phone number

