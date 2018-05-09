str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(":")

sppos = str.find("5",atpos)

host = str[atpos+1:sppos+1]
print(float(host))

