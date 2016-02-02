T = int(raw_input())
num =map(int,raw_input().split())
idx = int(raw_input())
i = len(num) - 1
for i in range(len(num) -1):
	k = num[(i + 1) % len(num)]
	print k



##########Forever circular list
# while True:
# 	for x in num:
# 		while 
# 		i += idx
# 		num.remove(x)
# 		print num
# 		if i > 100:
# 			break
# 		if len(num) == 1:
# 			break
		#print x Infinite circular loop



# #while int(len(num)) > idx:
# while i < len(num):
# 	if i == idx:
# 		num.pop(i)
# 		print num
# 	i += 1
# #	if i < len(num):
# #		i += 1
# #		if len(num) < idx:
# #			
# #			
# #	else:
# #		i = 0

# print num