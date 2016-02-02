t = int(raw_input())
for i in range(t):
	s = raw_input()
	for j in s[j:j+1]:
		if s[j] == s[j-1]:
			s.pop(j)
	print s