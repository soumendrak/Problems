import math
print 'Enter which serial prime number you want to find'
reqd = int(raw_input())
cnt,j = 0,2
print 'Enter until which number you want to find prime'
e = int(raw_input())
num = map(int,xrange(1,e))   		
limit = int(math.sqrt(len(num)))+ 1

for m in xrange(0,len(num)):	 		
		if num[m] != 0 and num[m] % j == 0 and num[m] != j:
			num[m] = 0
while j < limit:
	for m in xrange(0,len(num)):	 		
		if num[m] != 0 and num[m] % j == 0 and num[m] != j:
			num[m] = 0
	
	while j < limit:
		if j % 2 == 0:
			j += 1
		if j % 3 == 0:
			j += 2
		if j % 5 == 0:
			j += 2

# print num[:-500]
for k in xrange(0,len(num)):
	if num[k] != 0:
		cnt += 1
		if cnt == reqd:
			print 'the %d prime number is %d' %(reqd, num[k])
	if len(num)-1 == k and cnt < reqd:
		print 'the maximum prime# serial number is %d ' %cnt
		print 'you have to increase the maximum number limit to find the asked prime'
	
		