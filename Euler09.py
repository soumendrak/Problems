import math
for i in range(int(math.sqrt(1000))):
    y = 1000- i**2
    z = math.sqrt(y)
    if z.is_integer():
        print z