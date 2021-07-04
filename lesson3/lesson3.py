def bmi(height, weight):
    h = height / 100
    # code here
    print()
    return weight / (h * h)


def pi_1(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i * i + j * j <= n * n:
                cnt += 1
    # code here
    print()
    return cnt * 4 / (n * n)


def pi_2(n):
    result = 4
    plus_minus = -1
    for i in range(1, n):
        result += plus_minus + 4 / (i * 2 + 1)
        plus_minus *= -1
    # code here
    print()
    return result
