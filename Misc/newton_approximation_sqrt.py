epsilon = 0.1
k = 24.0
guess = k / 2.0

while abs(guess * guess - k) >= epsilon:
    guess -= (((guess**2) - k) / (2 * guess))

print('Square root of', k, 'is about', guess)
