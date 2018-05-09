# list can contain any type of values 
cheeses = ['Cheddar', "Edam", "Gouda"]
# a list within another list is nested
numbers = [17,34,23,[2,9,3]]
# a list with no elements is an empty list 
empty = []
print(cheeses, numbers, empty)

# indices start at 0 just like stings
print(cheeses[0])

# unlike strings list are mutable - can be changed 
numbers[1] = 5
print(numbers)

# in operator works 
if "Edam" in cheeses:
	print("yes")
else:
	print("no")
	
if 'Brie' in cheeses:
	print("yes")
else:
	print("no")

# traverse through loop
for cheese in cheeses:
	print(cheese)

# updating list note sublist repeat, counts of single element
for i in range(len(numbers)):
	numbers[i] = numbers[i]*2
print(numbers)



