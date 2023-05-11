un=input("enter the username : ").capitalize()
passw=input("enter the password : ").upper()

if un.replace(" ","")=="Studyonline" and passw=="SANDESH":
	print("valid user")
else:
	print("Invalid user")