t = ["b", "d", "a","c"]

# make copies 
orig = t[:]
t.sort()
print(t)

# correct 
t.append("x")
print(t)
t = t + ["y"]
print(t)

# wrong 
t.append(["q"])
print(t)

t = t.append("n")
print(t)

t = t + x
print(t)

t + ["t"]
print(t)



