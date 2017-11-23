inputList = [int(num) for num in input('Enter a sequence of integers: ')]


def findAnEven(listNumbers):
    """Assumes L is a list of integers Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
    for num in listNumbers:
        if num % 2 == 0:
            return num

    raise ValueError('Sequence not contain a even number!')


result = findAnEven(inputList)
print(result)
