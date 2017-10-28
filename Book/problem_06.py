epsilon = 0.1
k = 123456789
guess = k / 2.0

number_guess = 0
while abs(guess * guess - k) >= epsilon:
    guess -= (((guess**2) - k) / (2 * guess))
    number_guess += 1

print('Square root of', k, 'is about', guess)
print(number_guess)
