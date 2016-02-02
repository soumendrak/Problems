# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in xrange(T):
    N = long(raw_input())
    num = long(0)
    for j in xrange(3,N):
        if j % 3 == 0 or j % 5 == 0:
            num += j
            print j
    print num