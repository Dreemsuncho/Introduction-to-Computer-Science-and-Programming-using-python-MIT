input_count = 0

numbers = []

while input_count != 10:
    number = int(input('Add number: '))
    if number % 2 == 1:
        numbers.append(number)
    input_count += 1

max_odd_number = None
if len(numbers) > 0:
    max_odd_number = numbers[0]

for n in numbers:
    if max_odd_number is not None and max_odd_number < n:
        max_odd_number = n

if max_odd_number is not None:
    print(max_odd_number)
else:
    print('There is no odd number in the sequence')
