# count = 0
# S = raw_input()
# for i in range(2,len(S),3):
# 	if S[i-2:i] == 'SOS':
# 		pass
# 	else:
# 		if (S[i] != 'S'): 
# 			count += 1
# 		if (S[i-1] != 'O'):  
# 			count += 1
# 		if (S[i-2] != 'S'):
# 			count += 1
# print count

S=raw_input()
assert len(S)%3==0 and len(S)<=99
n=len(S)/3
exp="SOS"*n #Expected string
ans=0
for i in range(len(S)):
    if exp[i]!=S[i]:
        ans=ans+1
print ans