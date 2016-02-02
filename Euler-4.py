num1,num2,mul	=	0,0,0
for num1 in range(999,900,-1):
	for num2 in range(999,900,-1):
		mul		=	num1 * num2
		strmul	=	str(mul)
		if strmul[::]	==	strmul[::-1]:
			number	=	int(strmul)
			print "the number is %d" %(number)
		