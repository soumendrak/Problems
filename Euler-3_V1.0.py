# div2,counter = 0,2
print "Enter the number"
num	=	int(raw_input())

def process(num):
	div2,div1 = 0,0
	sumnum	=	sum(map(int, str(num)))
	print "sum of the digits of the number is %d" %(sumnum)
	newnum = divisibleby3(sumnum)
	
	for counter in range(2,num):
		if num % counter == 0:
			div1	=	counter
		# print "counter %d" %(counter)
		# print "div2 %d" %(div2)
		if div2	<	div1:
			div2=	div1		
	if div2 == 0:
		print "the largest prime factor is %d" %(num)
		return
	else:
		process(div2)
		return

def divisibleby3(int):
	while int % 3 == 0 or int / 3 != 0:
		int	=	int/3
	return int

process(num)
