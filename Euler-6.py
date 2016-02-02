i,m,n	=	1,0,0
for i in range(1,101):
	m	+=	i**2
	n	+=	i
print "the answer is %d" %(n**2 - m)
print "squares addition value %d" %(m)
print "addition squared is %d" %(n**2)