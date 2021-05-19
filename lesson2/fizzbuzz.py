#題目：寫一個程式，按照順序輸出1到100的數字。但是，數字為3的倍數時，就輸出『Fizz』而不要輸出數字，5的倍數時，就輸出『Buzz』，同時是3跟5的倍數時，則輸出『Fizzbuzz』

# #fizzbuzz01 先寫出 1到100
# for i in range(1, 101):
#     print(i, end=' ')

# #fizzbuzz02 再來判斷3的倍數
# for i in range(1, 101):
#     if i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i, end=' ')

# #fizzbuzz03 再來判斷5的倍數，此時15的倍數還是會先顯示Fizz 因為判斷式是先讓3的倍數被判斷
# for i in range(1, 101):
#     if i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0 :
#         print('Buzz')
#     else:
#         print(i, end=' ')

# #fizzbuzz04 同時是3跟5倍數顯示FizzBuzz 但這樣寫法不是最直觀的寫法
# for i in range(1, 101):
#     if i % 3 == 0:
#         if i % 5 ==0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')
#     elif i % 5 == 0 :
#         print('Buzz')
#     else:
#         print(i, end=' ')


#fizzbuzz05 最終板
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0 ):
        print('FizzBuzz', end = '')
    elif i % 3 == 0 :
        print('Fizz', end = '')
    elif i % 5 == 0 :
        print('Buzz', end = '')
    else:
        print(i, end=' ')