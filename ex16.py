data = "ABCBAB"
print(data.index("B"))

print(data.index("C"))

print(data.rindex("B"))
print(data.rindex("A"))


print(data.rindex("B",0,2))
#print(data.index("B",0,1))

print(data.index("B",0,6))