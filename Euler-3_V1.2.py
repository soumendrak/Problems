print "Enter the number"
num	=	int(raw_input())

def process(num):
	div2,div1,counter = 0,0,2
	while counter < num:
		if num % counter == 0:
			div1	=	counter
		if div2	<	div1:
			div2=	div1	
		counter += 1 
	# if div2 == 0:
		print "the largest prime factor is %d" %(num)
		# return
	# else:
		# process(div2)
		# return
	# sumnum	=	sum(map(int, str(num)))
	# print "sum of the digits of the number is %d" %(sumnum)

process(num)