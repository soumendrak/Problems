import math
t = int(raw_input())
for i in xrange(t):
	s,e = map(int,raw_input().split())		#starting and ending numbers
	num = map(int,xrange(s,e+1))   			#It has all the numbers given as input. we need to modify these.
	limit = int(math.sqrt(len(num)))+ 1
	for j in xrange(2,limit+2):	
		for m in xrange(0,len(num)):	 		
			if num[m] != 0 and num[m] != j and num[m] % j == 0 :
				num[m] = 0
	# print num
	for k in xrange(0,len(num)):
		if num[k] != 0:
			print str(num[k]) + '\n'
		
		