word = input()
count = 0
index = [ ]
for letter in word:
	if letter in index:
		count = count + 1
	index.append(letter)
print(count)
print (word)


	