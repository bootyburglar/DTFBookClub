input_year=input('請輸入1950年到2050年之間的年份：') #出來是字串
input_year_correct= int(input_year) #把字串轉數字

if input_year_correct in range(1950, 2051): #比較的是用 數字比
    
    if input_year_correct % 4==0 and  input_year_correct % 100 ==0 and input_year_correct % 400 == 0:
    
        print(input_year + " 年是閏年，因為它可以被4整除，並且也可以被100及400整除")
 
    elif input_year_correct % 4==0: #能被4整除但無法被100整除
    
        print(input_year + " 年是閏年，因為它可以被4整除，但不能被100整除")

    else:
        print(input_year + " 年不是閏年，它無法被4整除")

else :
    print('格式錯誤，請重新輸入')

