from functools import *


s="12,14,16,18,20".split(",")
ss=list(map(int,s))

sss=reduce((lambda n,j:j+n),ss)
ssss=sss/len(s)

print('{0:.4f}'.format(ssss)) 