s = raw_input().strip()
summ,q,z = 0,0,' '
for i in range(len(s)):
	summ = summ + ord(s[i])
	p = s.count(s[i])
	if p > q:
		q = p
		z = s[i]
		
w = int(round(float(summ) / len(s)) - 1)
if w % 2 == 0:
	print s[::-1]
else:
	print z
#print summ, w, z