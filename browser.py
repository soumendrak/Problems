T = int(raw_input())
for i in range(T):
	w,cnt = '',0
	w = raw_input()
	le = len(w)
	for j in range(le):
		if w[j] == 'a' or w[j] == 'e' or w[j] == 'i' or w[j] == 'u':
			cnt += 1
		elif w[j] == 'o' and w[j-2:j+2] != '.com':
			cnt += 1
		elif w[j:j+4] == 'www.':
			cnt += 4
	print str(le-cnt) + '/' + str(le)

