import re
fhand = open('actual.txt')
inp = fhand.read()
z = re.findall(r"[-+]?\d*\.\d+|\d+",inp)
y = map(int,z)
print y
print sum(y)
# y = [' '.join(int(s)) for s in z]
# print sum(z)
# cnt = 0
# z =[]
# for line in fhand:
# 	cnt += 1
# 	z = re.findall(r"[-+]?\d*\.\d+|\d+",fhand)
# 	if z != []:
# 		# print z
# 		y = ' '.join(z)
# 		print y
# 		z.append(y)
# 		print z
	# x = [int(s) for s in line.split() if s.isdigit()]
	# if x != []:
	# 	z.append(x)
# print cnt
# print z
# print sum(z)