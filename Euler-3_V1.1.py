# div2,counter = 0,2
print "Enter the number"
num	=	int(raw_input())

def process(num):
	div2,div1 = 0,0
	# newnum, div1	=	check(num,div1)
	newnum, div1	=	check()
	if div2	<	div1:
			div2=	div1		
	for counter in range(2,newnum):
		if newnum % counter == 0:
			div1	=	counter
		print "counter %d" %(counter)
		print "div2 %d" %(div2)
		if div2	<	div1:
			div2=	div1		
	if div2 == 0:
		print "the largest prime factor is %d" %(newnum)
		return
	else:
		process(div2)
		return


	return int

def check(num,div1):
	sumnum	=	sum(map(int, str(num)))
	print "sum of the digits of the number is %d" %(sumnum)
	lastdigit	=	num	% 10
	newnum 		=	num
	if sumnum % 3 == 0:
		while num / 3 == 0 and num != 3: 
			num,div1	=	num/3,3
		# check(num,div1)
	elif num % 2 == 0:
		while num / 2 == 0 and num != 2:
			newnum,div1 = num /2,2		
		# check(newnum,div1)
	elif lastdigit == 5:
		while num != 5:
			newnum,div1 = num /5,5
		# check(newnum,div1)
	elif num % 7 == 0:
		while num != 7:
			newnum,div1 = num / 7,7
		# check(newnum,div1)
	elif num % 11 == 0:
		while num != 11:
			newnum,div1 = num / 11,11
		# check(newnum,div1)
	else:
		return (newnum,div1)
	
process(num)
