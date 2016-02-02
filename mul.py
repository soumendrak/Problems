t = long(raw_input())
for i in range(t):
	mul = 1
	n = long(raw_input())
	for j in range(n,0,-1):
		mul = mul * j
	print mul
		