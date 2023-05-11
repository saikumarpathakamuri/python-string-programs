s = "Royal Enfield"
print(s)
s = s.split()
lst=[]
for i in s:
	k = i[::-1]
	lst.append(k)
print(" ".join(lst))