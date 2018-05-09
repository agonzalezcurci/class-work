def middle(t):
	return t[1: -1]

letters = ['a','b','c']
new = middle(letters)
print(new)

strings = ["Angela","Chris", "Lena", "Mariah"]
new = middle(strings)
print(new)

def chop(t):
	del t[0]
	del t[-1]

letters = ['a','b','c']
new = chop(letters)
print(new)

strings = ["Angela","Chris", "Lena", "Mariah"]
new = chop(strings)
print(new)
