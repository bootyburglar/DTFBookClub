#轉換基數
#目的：了解10進制和2進制之間的轉換
#      知道如何實做以及while進行重複
#      知道如何建立自己的函式

# # convert01 從10進制轉換為2進制
# # 這裡的關鍵在已經社好的字串前面附加文字，並且將所得到的商社為下一個被除數


# n=18
# result= ''
# while n > 0 :
#     result = str(n % 2) +result  #將餘數加到字串的左側
#     n //= 2 #將處以2所得的商再次帶入
# print(result)

# # convert02
# # 為了使它更加通用，來寫個轉換函式，讓我們可以指定基數。有這樣的函式，可以處裡基數2~10的轉換 


# n=18

# def convert(n, base):
#     result = ''

#     while n > 0:
#         result = str(n % base) + result
#         n //= base

#     return result

# print(convert(n, 2))
# print(convert(n, 3))
# print(convert(n, 8))

# # convert03 從2禁制轉換為10進制
# # 說明：首先，for循環使用len函式，使重複次數相當於輸入的字元數。在迴圈之中，要從字串的開頭一次取出一個字元，並且將其乘上基數的次方運算結果。現在我們計算的是2進位術的轉換所以基數為2，因此在計算次方時，i=0時是4次方，i=1時是3次方，i=2時是2次方，以此類推，算出次方的部份


# n='10010'

# result = 0
# for i in range(len(n)):
#     result +=int(n[i]) *(2 ** (len(n) - i -1 )) # 第一段int部份 一次取出一個字元 第二部份 len(n) 計算次方部份

# print(result)

# # convert04 內建使用10轉2進制 （bin函式） 以及2轉10進制 （int函式）
# #平常2進制都被視為字串處裡，但是如果在開頭加上0b，則可以將其作為整數型別處裡

# a=18
# print(bin(a))

# b='10010'
# print(int(b, 2))


#以下有常用的位元運算
c= 0b10010
print(bin(~c))
d=0b11001
print(bin( c & d))
print(bin( c | d))
print(bin( c ^ d))
print(bin( c << 1))
print(bin( d >> 2))