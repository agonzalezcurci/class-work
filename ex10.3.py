# unique about tuples can have tuple on left side of an assignment statment 
m = ["have", "fun"]
(x,y) = m
print(x)
print(y)

# allows for the swapping of values in a statement 
x,y = y,x

print(x)
print(y)

# use: split email address into username and domain 
addr = "monty@python.org"
uname, domain = addr.split("@")

print(uname)
print(domain)