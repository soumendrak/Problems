t = int(raw_input())
a,b,c=[],[],[]
w=0
for i in range(t):
	try:
		x,y,d = map(int,raw_input().split(' '))
		if c == d and a == x and b == y:
			pass
		else:
			# a,b,c = x,y,d
			# a[i] = 1
			a.append(x)
			b.append(y)
			c.append(d)
			print a[i]
			print b
			print c
			w = w + d + 1
	except (EOFError):
   		break #end of file reached
#		for j in range(x,(x + d+ 1)):
#			w += 1
print w
		