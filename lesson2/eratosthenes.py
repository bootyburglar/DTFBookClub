
#思考如何快速找出質數
# #eratosthenes.py

# #這個方式就是在指定範圍內將可被2整除的數、可被3整除的數…等可被整除的術都暗順序排除

# import math


# def get_prime(n):
#     if n <=1:
#         return []
#     prime = [2]
#     limit = int(math.sqrt(n))

#     #建立奇數串列
#     data = [i + 1 for i in range(2, n, 2)]
#     while limit >= data[0]:
#         prime.append(data[0])
#         #只取出無法整除的數字
#         data = [j for j in data if j % data[0] !=0]


#     return prime + data

# print(get_prime(200))

#用這個方法同樣搜尋100,000以內的質數，只需要0.1秒不到。找的範圍月大石，差距也會跟著變大

# Python有個 SymPy函式庫，可以更輕易地處裡質數的問題
#安裝SymPy函式庫
# > pip install sympy

# #sympy01.py

# from sympy import sieve

# print([i for i in sieve.primerange(1, 200)])   #求質數

#sympy02,py

from sympy import isprime

print(isprime(101))  #判斷是否為質數