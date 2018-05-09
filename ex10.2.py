#DSU 

#Decorate: Build list of tuples w/ one or more keys preceding elements in the sequence 
#This loop builds a list of tuples where each tuple is proceeded by its length

txt = "but soft what light in yonder window breaks"
words = txt.split()
t = list()
for word in words: 
	t.append((len(word),word))
#Sort:  sort using built in  using words 
# This sort compares length first, then considers A-Z word to break ties in decreasing order
 
t.sort(reverse= True)

# Undecorate: extract sorted elements of the sequence 
# builds a list of words in descending order of length, then reverser A-Z order

res = list()
for length, word in t:
	res.append(word)
print(res)
