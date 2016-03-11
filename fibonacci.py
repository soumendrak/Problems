# def facto(number):
#     if number   ==  0:  return 1
#     else:
#         return number*facto(number-1)
#     
# number  =   int(raw_input('Input the number>'))
# print facto(number)

def fibo(number):
    if number   ==  0:  return 0
    if number   ==  1:  return 1
    return  fibo(number-1) + fibo(number-2)

number  =   int(raw_input('Input the number>'))
print fibo(number)
