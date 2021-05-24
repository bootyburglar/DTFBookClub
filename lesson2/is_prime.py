#判斷是否為質數
#目的：
# 學會使用數學函式庫
# 學會使用串列推導式


#寫一個判斷質數的程式

# # is_prime01

# import math # 引入數學模組以計算平方根

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):   #計算平方根
#         if n % i ==0:     #判斷是否可整除
#             return False  #可整除則非質數
#     return True          #無法被任何一個數字整除的話就是質數

#
# is_prime02   用上面的程式可以來寫一個輸出1~200整數中的質數


import math # 引入數學模組以計算平方根

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):   #計算平方根
        if n % i ==0:     #判斷是否可整除
            return False  #可整除則非質數
    return True          #無法被任何一個數字整除的話就是質數

for i in range(200):
    if is_prime(i): #呼叫上面定義的函式
        print(i, end=' ')

# 這方法雖然簡單，但只要搜索範圍變大，就得花很久時間計算。在此環境中，搜尋100,000之內的質數大約需要0.5秒