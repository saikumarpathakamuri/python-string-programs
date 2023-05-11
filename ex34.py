s = "8"#input("enter any character : ")
print(s)
if s.isalnum():
	print("given character is alphanumeric")
	if s.isalpha():
		print("given character is alphabet")
		if s.islower():
			print("given character is lowercase alphabet")
		else:
			print("given character in uppercase alphbet")
	else :
		print("given character is digit number")
elif s.isspace():
	print("given character is space")
else:
	print("given character is special number ")