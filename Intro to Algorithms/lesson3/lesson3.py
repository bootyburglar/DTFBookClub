"""
請考慮下面三個程式以下的複雜性在用 print 寫出來
"""


# 根據身高和體重計算 BMI(表示肥胖程度的體格指數)得函式
def bmi(height, weight):
    h = height / 100
    # code here
    print("O(1)")
    return weight / (h * h)


# 計算圓周率近似值的函式
# 計算在正方形中,落在扇形範圍的數字的數量
def pi_1(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i * i + j * j <= n * n:
                cnt += 1
    # code here
    print("O(N^2)")
    return cnt * 4 / (n * n)


# 計算圓周率近似值的函式
# pi 可以用4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...的式子計算
def pi_2(n):
    result = 4
    plus_minus = -1
    for i in range(1, n):
        result += plus_minus + 4 / (i * 2 + 1)
        plus_minus *= -1
    # code here
    print("O(N)")
    return result
