t = int(raw_input())
for a in range(t):
    n = int(raw_input())
    sum,i,j = 0,1,2
    while i < n:
        i = i + j
        print i,j
        if i > 4:
            j = i - j
	    if i % 2 == 0 and (sum + i) < n:
		    sum = sum + i		
    print sum + 2
	