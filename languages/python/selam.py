def comb(n, r):
    result = 1
    for i in range(n, n-r, -1):
        result *= i
    for i in range(r, 0, -1):
        result /= i

    return result

def func(n):
    c = comb(35, n)
    x = (0.1)**n
    y = (0.9)**(35-n)
    return c*x*y


result = 1

for i in range(11):
    result -= func(i)

print(result)