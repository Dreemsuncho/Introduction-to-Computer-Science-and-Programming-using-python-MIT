text = input('Enter text: ')
part = input('Enter text to be search: ')


def isIn(text, part):
    """Print and return true or false whether text contains part"""
    result = part in text
    print(result)
    return result


isIn(text, part)
