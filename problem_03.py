input_number = int(input('Enter an integer: '))

pwr = 2
has_pairs = False
for root in range(1, 6):
    if root ** pwr == input_number:
        print('root is : ', root)
        print('pwr is : ', pwr)
        has_pairs = True

if not has_pairs:
    print('No such pair of integers exist')
