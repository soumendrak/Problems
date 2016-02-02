#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# i,numb	=	20,0	
# for i in range(5040,100000000,1):
	# numb	=	20	* 	i	
	# # i		+=	1
	# if numb	% 2520 == 0 and numb % 11 == 0 and	numb % 12 == 0 and	numb % 13 == 0 and numb % 14 == 0 and numb % 15 == 0 and numb % 16 == 0 and numb % 17 == 0 and numb % 18 ==0 and numb % 19 ==0:
		# print "the number is %d" %(numb)
		# break

i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
			# print i
			# print j 
			# print k
            if (i*j) % k == 0:
                i *= j
                break
print i
