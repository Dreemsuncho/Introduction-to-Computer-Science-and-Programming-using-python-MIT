s = '1.23,2.4,3.123'

total = 0
for num in s.split(','):
    total += float(num)

print(total)
