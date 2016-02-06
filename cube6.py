# 9.
# (Oops)Which of these helps in determining the method to invoke at run time?
# 
# Max. Marks 10.0 
#  Data hiding
#  Dynamic Typing
#  Dynamic binding
#  Dynamic loading

# 10.
# (Oops)Which of these helps in achieving Runtime polymorphism?
# 
# Max. Marks 10.0 
#  Friend function
#  Virtual function
#  Operator overloading
#  Function overloading




# 11.
# Milly and Chocolates III (Mandatory)
# Max. Marks 200
# Milly loves chocolates very much. She is at the land of chocolates. This land has N rooms such that there are some chocolates of different brands in every room. It is possible that there can be multiple chocolates of same brand in a particular room. Now she is in a dilemma that whether she can eat at least K distinct branded chocolates at least once. Your task is to print the minimum number of rooms she must visit to eat at least those K distinct brands at least once.
# 
# Note : Once she enters a particular room, she will eat all of the chocolates available in that room.
# 
# Input
# 
# First line of the input will contain a integer T (number of test cases).
# Then for every test case there will be one line containing the values of N (denoting the number of rooms) and K separated by a space.
# Now each of the next N lines will first have a value P then P space separated strings denoting the names of the brands.
# Output
# 
# For every test case, print the required answer and if it is not possible to eat those K distinct chocolates then print -1.
# Constraints
# 1 <= T <= 3
# 1 <= N <= 16
# 1 <= K <= 40
# 1 <= P <= 10
# 1 <= Length of the strings <= 10
# Sample Input(Plaintext Link)
#  1
# 3 2
# 1 KITKAT
# 2 FIVESTAR KITKAT
# 2 KITKAT PERK
# Sample Output(Plaintext Link)
#  1
# Time Limit: 2 sec(s) for each input file.
# Memory Limit: 256 MB
# Source Limit: 1024 KB
# Marking Scheme: Marks are awarded if any testcase passes.
# Allowed languages: PYTHON





# T = int(raw_input())
# for _ in range(T):
#     N,K = map(int,raw_input().split())
#     choc = []
#     for i in range(N):
#         choc.append(list(set(raw_input()[2:].split())))
#         print choc
#         if len(choc) >= K:
#             print '1'

# a = (2,4,5)
# print a
# c = [2|4|5]
# print c #Could not get it

# 12.
# Professor Hatim's Experiment (Mandatory)
# Max. Marks 200
# Professor Hatim is researching the sexual behavior of a rare species of lizard. He assumes that they feature two different genders and that they only interact with lizard of the opposite gender. Each lizard has a integer printed on their back.
# 
# Given the details of lizard interactions, decide whether the experiment supports his assumption of two genders with no homosexual bugs, or if it contains some bug interactions that falsify it. Or simply, you have to print "Suspicious lizard found!" (without quotes), if an interaction of two lizards of same gender is found in the list of interactions, otherwise print "No suspicious lizard found!" (without quotes).
# 
# Input format:
# The first line contains an integer T, denoting the number of test cases.
# The first line of each test case contains two integers N and M, where N denotes the number of lizards and M denotes the number of interactions.
# Next M lines of each test case contains, two space separated integers, say x and y , denoting the interaction between lizard no. x and lizard no. y.
# 
# Note: Integers on the back of lizards are numbered from 1 to N.
# 
# Output format:
# For each test case ,print a line, saying either “No suspicious lizard found!” if the experiment is consistent with his assumption about the lizard sexual behavior, or “Suspicious lizard found!” if Professor Hatims’s assumption is definitely wrong.
# 
# Constraints:
# 1 ≤ T ≤ 5
# 2 ≤ N ≤ 2000
# 1 ≤ M ≤ 105
# 
# Sample Input(Plaintext Link)
#  2
# 3 3
# 1 2
# 2 3
# 1 3
# 4 2
# 1 2
# 3 4
# Sample Output(Plaintext Link)
#  Suspicious lizards found!
# No suspicious lizards found!
# Time Limit: 1 sec(s) for each input file.
# Memory Limit: 256 MB
# Source Limit: 1024 KB
# Marking Scheme: Marks are awarded if any testcase passes.
# Allowed languages: PYTHON

# 13.
# SALE (Optional)
# Max. Marks 100
# There is a sale in the market on clothes , so as usual N girls gathered there to grab great deals.But due to huge popularity of sale crowd has gone uncontrollable. You being head of management team of the mall has been assigned the task to make them form a queue so that everyone can shop turn-wise. Since queue is going to be very long and knowing that its gonna take time for their turn there are M pair of girls who want to stand together in the queue so that they can discuss their personal stuff meanwhile. Now you need to make them form a queue so that none of them gets disappointed.
# 
# INPUT:
# 
# First line of input contains T number of test-cases , first line of each test-case contains two elements N , M total number of girls and number of pair of girls who wants to stand together. Next M line will contain pair of integers x y , which mean in queue they either stand as x y or y x .
# 
# OUTPUT:
# 
# For each test-case in a new line output "NO" ( without quotes ) if there is no possible arrangement such that no one gets disappointed if such a arrangement is possible print "YES" ( without quotes ) .
# 
# Constraints:
# 
# 1 ≤ T ≤ 10
# 
# N , M ≤ 10 ^ 5
# 
# Sample Input(Plaintext Link)
#  2
# 5 3
# 1 2
# 3 4
# 2 5
# 4 3
# 1 2
# 1 3
# 1 4
# Sample Output(Plaintext Link)
#  YES
# NO
# Time Limit: 1 sec(s) for each input file.
# Memory Limit: 256 MB
# Source Limit: 1024 KB
# Marking Scheme: Marks are awarded if any testcase passes.
# Allowed languages: PYTHON
# 
# 14.
# Shil and weird equation (Optional)
# Max. Marks 300
# Shil came across a weird equation and he wants to find out total number of solutions of this equation.The weird equation is :
# x1+ x2 + x3 ... xN = D .
# Find total number of solutions of this equation such that each xi are non-negative and gcd of all the xi is one.Here gcd stands for greatest common divisor.
# Assume that gcd(0,y) = y for any y.
# 
# Input:
# Only line of input consists of two integers N and D .
# 
# Output:
# Output total number of solutions modulus 109+7
# 
# Constraint:
# 1 ≤ N ≤ 104
# 1 ≤ D ≤ 104
# 
# Sample Input(Plaintext Link)
#  3 2
# Sample Output(Plaintext Link)
#  3
# Explanation
# All the possible cases are:
# 1.) x1=1 , x2=0 , x3=1
# 2.) x1=1 , x2=1 , x3=0 
# 3.) x1=0 , x2=1 , x3=1
# 
# Time Limit: 1 sec(s) for each input file.
# Memory Limit: 256 MB
# Source Limit: 1024 KB
# Marking Scheme: Marks are awarded if any testcase passes.
# Allowed languages: PYTHON