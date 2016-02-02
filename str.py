# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
l = []
for i in range(t):
    s = raw_input()
    if s.find('insert') > -1:
        splt = s.split(' ')
        u = int(splt[len(splt) - 1])
        v = int(splt[len(splt) - 2])
        l.insert(v, u)
    elif s.find('append') > -1:
        splt = s.split(' ')
        u = int(splt[len(splt) - 1]) 
        l.append(u)
    elif s.find('remove') > -1:
        splt = s.split(' ')
        u = int(splt[len(splt) - 1]) 
        l.remove(u)
    elif s.find('sort') > -1:
        l.sort()
    elif s.find('print') > -1:
        print l
    elif s.find('pop') > -1:
        l.pop()
    elif s.find('reverse') > -1:
        l.reverse()   