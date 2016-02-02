t = int(raw_input())
for i in range(t):
	s = list(raw_input())
	print s
	p = s[0]
	for j in range(1,len(s)):
		if s[j] != s[j-1]:
			p += s[j]
	print p