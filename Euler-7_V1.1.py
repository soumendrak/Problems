#Finding the 10001st prime number
i,j,k=2,0,2
a=[0,0]
# while j < 10:
for k in range(2,2000):
		#increase k from 2 to n number 
		for i in range(2,2000):
			a[i]	=	i
			if a[i] % k == 0:
				a[i]	=	0
			# elif a[k] != 0 and a[k] <= i:
				# j += 1
print a[i]			
		
	# DEF SDF():
		
