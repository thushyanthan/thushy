a=list(map(int,input().split(" ")))
b=set(a)
c=[]
for i in b:
	if a.count(i)==1:
		c.append(i)
if len(c)>=1:
	print(*c)
else:
	print("0")
