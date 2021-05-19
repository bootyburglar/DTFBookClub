import sys
coins = {
    '5000':1000,
    '1000':1000,
    '500':1000,
    '100':1000,
    '50':1000,
    '10':1000,
    '1':1000
}

def give_change(insert,buy):
    if insert > buy:
        change = insert - buy
        change_detail = {}
        for coin,cnt in coins.items():
            coin_cnt,change = divmod(change,int(coin))
            if not coin_cnt:continue
            change_detail.update({coin:coin_cnt})
        print(change_detail)
    else:
        print('餘額不足')

def run():
    try:
        buy_money = int(input('買幾錢'))
        insert_money = int(input('投幾錢'))
        give_change(insert_money,buy_money)
    except Exception as e:
        print('機器發生錯誤')
        print(e)

if __name__ == '__main__':
    while True:
        run()
        if input('離開請q') == 'q':
            print('掰掰8888')
            sys.exit()