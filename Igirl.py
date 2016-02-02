s = map(int,raw_input())
ans = []
for i in range(len(s)):
	cnt = 0
	for j in range(i,len(s)):
		if s[j] % 2 == 0:
			cnt += 1
	print cnt
	ans.append(cnt)
print ans