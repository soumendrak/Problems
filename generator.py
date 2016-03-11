# '''
# Created on Mar 6, 2016
# 
# @author: Soumendra
# '''
# 
# class inclusive_range:                              #The class is specified with no arguments however it takes one argument
#     """docstring for inclusive_range"""
#     def __init__(self, *args):                      #This the constructor by default being called when the Class is called.
#         numargs    =    len(args)
#         if numargs < 1:
#             raise TypeError('requires at least one argument')
#         elif numargs    ==    1:
#             self.start    =    0
#             self.stop    =    args[0]
#             self.step    =    1
#         elif numargs     ==    2:
#             self.start, self.stop    =    args
#             self.step    =    1
#             if self.start > self.stop:
#                 raise TypeError('Start value should be less than the stop value')
#         elif numargs    ==    3:
#             self.start, self.stop, self.step    =    args
#             if self.start > self.stop:
#                 raise TypeError('Start value should be less than the stop value')
#         else:
#             # raise TypeError('At most three arguments require, %d given') %numargs
#             raise TypeError('At most three arguments require, {} given'.format(numargs))
# 
#     def __iter__(self):                             #It's an iterator, iterates over a value and returns the same
#         i     =    self.start
#         while i <= self.stop:
#             yield    i                              #Yield returns the current value, when __iter__ being called again it returns the value which was there before, however return again begins from the beginning.
#             i += self.step
#         
# def main():
#     # o = range(25)
#     for i in inclusive_range(1,2,3): print i, 
# 
# if __name__ == "__main__": main()
# def gen(n):
#     
#     while n < 10:
#         return n
#         n +=    1
#         
# g = gen(6)
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# function version
def fibon(n):
    a = b = 1
    result = []
    for _ in xrange(n):
        result.append(a)
        a, b = b, a + b
    return result

g = fibon(10)
print g

def fibon1(n):
    a = b = 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b
        
h = fibon1(10)
print h.next()