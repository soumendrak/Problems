sum,i,j = 0,1,2
while i < 4000000:
	# print "the value of j is %d" %(j) 
	i = i + j
	print "the value of i is %d" %(i) 
	if i > 4:
		j = i - j
	if i % 2 == 0:
		sum = sum + i		
print "the sum of even valued terms are %d" %(sum + 2) 
	