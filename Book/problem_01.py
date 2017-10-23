x = int(input('Enter x number: '))
y = int(input('Enter y number: '))
z = int(input('Enter z number: '))

numbers = []

if x % 2 == 1:
    numbers.append(x)
if y % 2 == 1:
    numbers.append(y)
if z % 2 == 1:
    numbers.append(z)

if len(numbers) > 0:
    print(max(numbers))
else:
    print('No provided odd values')
