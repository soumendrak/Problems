# # # from collections import Counter as cnt
# # # # w= raw_input('Enter your word>')
# # # w = 'soumendra kumar sahoo'
# # # print cnt(w)
# # # print cnt(w).most_common(1)
# # # print sum(cnt(w).values()) 
# # 
# # class pilu:
# #     def __init__(self, value):
# #         print 'constructor'
# #         self.val = value
# #     
# #     
# #     def eat(self):
# #         print 'Pilu is eating %d \n' %self.val
# #         
# #         
# #     def drink(self):
# #         print 'Pilu is drinking %d' %self.val
# #     
# # who = pilu(99)
# # who.eat()
# # who.drink()
# # # print who.__module__
# # # # print who
# # # print dir(who)
# 
# 
# 
# S   =   list(raw_input())
# x, y =   0, 0
# final = []
# for i in range(len(S)):
#     if S[i] ==  'N':
#         y +=    1
#     elif S[i]   ==  'E':
#         x +=    1
#     elif S[i]   ==  'S':
#         y -=    1
#     elif S[i]   ==  'W':
#         x -=    1
# 
# print x,y
# if x < 0:
#     final.append('W' * abs(x))
# elif x > 0:
#     final.append('E' * abs(x))
# if y < 0:
#     final.append('S' * abs(y))
# elif y > 0:
#     final.append('N' * abs(y))
#     print final
# print ''.join(final)
L = int(raw_input())
S = map(int,raw_input().split()).sort()
M = int(raw_input())
