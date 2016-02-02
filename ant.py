t = int(raw_input())
a,b,c=[],[],[]
w=0
for i in range(t):
	try:
		x,y,d = map(int,raw_input().split(' '))
		a.append(x)
		b.append(y)
		c.append(d)
		w = w + d + 1
	except (EOFError):
   		break 
print a,c
print zip(a,c)
print w
		