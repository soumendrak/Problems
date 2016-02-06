# # t = int(raw_input())
# # for i in range(t):
# # 	s = list(raw_input())
# # 	print s
# # 	p = s[0]
# # 	for j in range(1,len(s)):
# # 		if s[j] != s[j-1]:
# # 			p += s[j]
# # 	print p
# # camel = 12
# # print 'I have spotted %d camels today at Rajasthan' % camel
# # print 'Hello \nworld'
# # print 'my name' + '\n' + 'is' + ' pilu'
# # ls = ['a','x','z','c'] + ['a']
# # # z = ls.pop()
# # print ''.join(ls)
# 
# # t1 = [1,2,3]
# # t3 = t1 + [3]
# # print t3
# # print map(chr,range(1,256))
# import datetime
# now = datetime.datetime.now()
# 
# print
# print "Current date and time using str method of datetime object:"
# print str(now)
# 
# print
# print "Current date and time using instance attributes:"
# print "Current year: %d" % now.year
# print "Current month: %d" % now.month
# print "Current day: %d" % now.day
# print "Current hour: %d" % now.hour
# print "Current minute: %d" % now.minute
# print "Current second: %d" % now.second
# print "Current microsecond: %d" % now.microsecond
# 
# print
# print "Current date and time using strftime:"
# print now.strftime("%Y-%m-%d %H:%M")
# 
# print
# print "Current date and time using isoformat:"
# print now.isoformat()

T = int(raw_input())
for _ in range(T):
    N,K = map(int,raw_input().split())
    choc = []
    for i in range(N):
        choc.append(list(set(raw_input()[2:].split())))
        print choc
        if len(choc) >= K:
            print '1'
#             break
#     choc = list(set(choc))
#     print choc