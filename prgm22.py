s="Sandesh@6460"
l,u,d,sp=0,0,0,0
for i in s:
	
	if i.islower():
		l=l+1
	elif i.isupper():
		u=u+1
	elif i.isdigit():
		d=d+1
	else:
		sp=sp+1

print("lower cases of strings occured : ",l," times")
print("upper cases of strings occured : ",u," times")
print("digits of strings occured : ",d," times")
print("special character of strings occured : ",sp," times")