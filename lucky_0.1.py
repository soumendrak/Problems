T = long(raw_input())
p = 0 
for p in xrange(T):
	j,i,cnt,s,k = 0,0,0,0,'' 
	N = long(raw_input())
	for j in xrange(N+1):
		B = bin(j)
		B = long(B[2:])
		L = map(long,str(B))
		le = len(L)
		i,cnt = 0,0 
		while i < le and cnt < 3:
			if L[i] == 1:
				cnt += 1				
			i += 1
		if cnt == 2:
			s += j
			k = s % 1000000007
	print k