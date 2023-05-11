s1 = "sandesh"
s2 = "suhas"
s3 = "Sandesh"
s4 = "suhas"
s3 = s3.lower()
 
print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))

if s1 == s2:
	print("string values are equal")
else:
	print("string values are not equal")

if s1 == s3:
	print("string values are equal")
else:
	print("string values are not equal")

if s1 is s2:
    print("Adress are equal")
else:
    print("Adress are not equal") 


if s4 is s2:
    print("Adress are equal")
else:
    print("Adress are not equal") 


if s1.upper() == s3.upper():
    print("Adress are equal")
else:
    print("Adress are not equal") 

