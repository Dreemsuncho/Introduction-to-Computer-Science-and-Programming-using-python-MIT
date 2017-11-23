s = input('Enter a word: ')


def sumDigits(str):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    sumNumbers = 0

    for ch in str:
        try:
            sumNumbers += int(ch)
        except:
            continue
    return sumNumbers


result = sumDigits(s)
print(result)
