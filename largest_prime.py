import math
print 'Enter the number, whose largest prime you need'
e = int(raw_input())
f = int(math.sqrt(e)) + 2
num = map(int,xrange(1,f))   		
for j in xrange(2,len(num)):	
	if e % num[j] == 0:
		for m in xrange(2,j+1):	 		
			if num[j] != m and num[j] % m == 0 :
				num[j] = 0
	else:
		num[j] = 0
num.sort()
print num[-1]