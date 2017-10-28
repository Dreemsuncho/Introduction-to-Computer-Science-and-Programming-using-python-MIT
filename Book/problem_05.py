x = float(input('Enter number to find a cube root: '))
epsilon = 0.0001
num_guesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (low + high) / 2.0

while abs(ans**3 - abs(x)) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1

    if ans**3 < abs(x):
        low = ans
    else:
        high = ans

    ans = (low + high) / 2.0

if x < 0:
    print(-ans, 'is close enugh to the cube root of', x)
else:
    print(ans, 'is close enugh to the cube root of', x)
