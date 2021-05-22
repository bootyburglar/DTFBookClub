# # 題目：設定自動販賣機的找零計算
# # 訓練：支援鍵盤輸入。
# #      處裡非法輸入。
# #      能夠使用串列寫出簡潔的程式

# # # vending_machine1
# # # 說明：先設計個可以輸入投入金額及輸入商品金額，最後會列印出找錢金額的程式
# # insert_price = input('insert: ') #接受輸入投入金額
# # product_price = input('product: ') #接受輸入商品金額
# # change = int(insert_price) - int(product_price)
# # print('change: ', int(change))

# # # vending_machine2

# # #計算找零金額，用最土砲的方式硬解出來  

# # insert_price = input('insert: ') #接受輸入投入金額
# # product_price = input('product: ') #接受輸入商品金額
# # change = int(insert_price) - int(product_price)
# # print('change: ', int(change))
# # #計算 1000元紙鈔的數量
# # r1000 = change // 1000
# # q1000 = change % 1000
# # print('1000: ' + str(r1000))

# # #計算 500元紙鈔的數量
# # r500 = q1000 // 500
# # q500 = q1000 % 500
# # print('500: ' +str(r500))

# # #計算 100元紙鈔的數量
# # r100 = q500 // 100
# # q100 = q500 % 100
# # print('100: ' + str(r100))

# # #計算 50元硬幣的數量
# # r50 = q100 // 50
# # q50 = q100 % 50
# # print('50: ' + str(r50))

# # #計算 10元硬幣的數量
# # r10 = q50 // 10
# # q10 = q50 % 10
# # print('10: ' + str(r10))

# # #計算 5元硬幣的數量
# # r5 = q10 // 5
# # q5 = q10 % 5
# # print('5: ' + str(r5))

# # #計算 1元硬幣的數量
# # print('1: ' + str(q5))


# # vending_machine3
# # 使用串列和迴圈讓實做更簡潔

# insert_price = input('insert: ') #接受輸入投入金額
# product_price = input('product: ') #接受輸入商品金額
# change = int(insert_price) - int(product_price)
# print('change: ', int(change))
# coin = [1000, 500, 100, 50, 10, 5, 1]

# for i in coin:
#     r= change //i 
#     change %= i #change= change % i
#     print(str(i) + ': ' + str(r))

# # vending_machine4
# # 應對不當輸入 引入 sys 模組

# import sys #引入模組，發生錯誤時可以用來強制結束

# input_price = input('insert: ') #接受輸入投入金額
# if not input_price.isdecimal():
#     print('錯誤：請輸入整數，請重新開啟此程式')
#     sys.exit() # 發生錯誤時強制結束
# product_price = input('product: ') #接受輸入商品金額
# if not product_price.isdecimal():
#     print('錯誤：請輸入整數，請重新開啟此程式')
#     sys.exit() # 發生錯誤時強制結束
# change = int(input_price) - int(product_price)

# if change < 0:
#     print('錯誤：金額不足，請重新開啟此程式')
#     sys.exit() # 發生錯誤時強制結束

# print('change: ', int(change))
# coin = [1000, 500, 100, 50, 10, 5, 1]

# for i in coin:
#     r= change //i 
#     change %= i #change= change % i
#     print(str(i) + ': ' + str(r))

# vending_machine5
# 介紹 divmod函式
# 函式 divomd 可以同時取得商與餘數。這個函式會將商和餘數成對回傳。 但其他語言無法使用這方法

import sys #引入模組，發生錯誤時可以用來強制結束

input_price = input('insert: ') #接受輸入投入金額
if not input_price.isdecimal():
    print('錯誤：請輸入整數，請重新開啟此程式')
    sys.exit() # 發生錯誤時強制結束
product_price = input('product: ') #接受輸入商品金額
if not product_price.isdecimal():
    print('錯誤：請輸入整數，請重新開啟此程式')
    sys.exit() # 發生錯誤時強制結束
change = int(input_price) - int(product_price)

if change < 0:
    print('錯誤：金額不足，請重新開啟此程式')
    sys.exit() # 發生錯誤時強制結束

print('change: ', int(change))
coin = [1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r, change = divmod(change, i)
    print(str(i) + ': ' + str(r))