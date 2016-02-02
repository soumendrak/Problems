# num = long(raw_input())
num = 73167176531330624919225119674426574742355349194934969835
# length = len(num)
prd = []
largest = 0
for i in xrange(0,1000,13):
	prd[i] = int(num[i] * num[i+1] * num[i+2] * num[i+3] * num[i+4] * num[i+5] * num[i+6] * num[i+7] * num[i+8] * num[i+9] * num[i+10] * num[i+11] * num[i+12])
	# prd[i] = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 8 * 7 * 6 * 5
	if prd[i] > largest:
		largest = prd[i]
		print num[i:14]
	else:
		pass
print 'the value of the product is %d' %largest