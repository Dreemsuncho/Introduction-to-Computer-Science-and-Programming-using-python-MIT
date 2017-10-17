x, y, z = 3, 2, 1

if(x % 2 == 1 and
   x >= y and
   x >= z):
    print(x)
elif (y % 2 == 1 and
      y >= x and
      y >= z):
    print(y)
elif (z % 2 == 0):
    print(z)
else:
    print('No odd values')
