#請寫一個函式，以參數方式給定西元年份時，轉換程日本的年號

year = input('請輸入1869年以上2020年以下的年份')

year_int=int(year)

def year_tasble(year):
    if year_int in range(1868, 1912):
        print('你輸入的是西元'+ year +'此年為明治'+ str(year_int-1867)+'年' ) 
    elif year_int in range(1912, 1926):
        print('你輸入的是西元'+ year +'此年為大正'+ str(year_int-1911)+'年' ) 
    elif year_int in range(1926, 1989):
        print('你輸入的是西元'+ year +'此年為昭和'+ str(year_int-1925)+'年' )
    elif year_int in range(1989, 2019):
        print('你輸入的是西元'+ year +'此年為平成'+ str(year_int-1988)+'年' )
    elif year_int in range(2019, 2021):
        print('你輸入的是西元'+ year +'此年為令和'+ str(year_int-2018)+'年' ) 
    else:
        print('輸入格式錯誤，無法判斷')

year_tasble(year)
