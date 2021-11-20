
def reverse(x: int) -> int:
    MAX = 2**31-1
    MIN = -2**31
    sign = x > 0
    if sign:
        result = int(str(x)[::-1])
    else:
        result = int(str(-x)[::-1]) * -1
    if (MIN <= result <= MAX):
        return result
    return 0


print(reverse(-123))