x = -25
epsilon = 0.01
step = epsilon**2
num_guesses = 0
low = 0.0
high = max(1.0, x)
ans = (low + high) / 2.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    print('low =', low, 'high =', high, 'and =', ans)
    num_guesses += 1

    if ans**2 < x:
        low = ans
    else:
        high = ans

    ans = (low + high) / 2.0

print('num guesses: ', num_guesses)
print(ans, 'is close to square root of', x)
