#find the 10001st prime number

print "Enter the number"
primenum	=	int(raw_input())

def process(primenum):
	counter,prime = 0,0
	while prime < primenum:
		for counter in range(1,1000):
			if num % counter == 0:
				div1	=	counter
			if div2 > div1:
				div2 	=	div1
		if div2 == 0:
			print "the largest prime factor is %d" %(primenum)
			prime += 1
		else:
			process(div2)
	print "The 10th prime number is %d" %(primenum)
	return int
