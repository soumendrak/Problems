# t = int(raw_input())
# for i in range(t):
# 	s = raw_input()
# 	for j in s[j:j+1]:
# 		if s[j] == s[j-1]:
# 			s.pop(j)
# 	print s

import math
N = list(str(math.factorial(int(10))))
cnt = 0
for i in range(1,len(N)):
	if N[-i] == '0':
		cnt += 1
		print N[-i]
	else:
		break
print cnt
		