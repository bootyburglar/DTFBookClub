def convert(num,base):
    ret=''
    while num >0:
        num,leave = divmod(num,base)
        ret = str(leave) + ret
    return ret

def run():
    print('1 :10進位轉換成？進位')
    print('2 :？進位轉換成10進位')
    choose = input('choose: ')
    if  choose== '1':
        print(convert(int(input('10進位: ')),int(input('想轉換成: '))))
    elif choose=='2':
        print(int(input('數值: '),int(input('數值是多少進位: '))))
    else:
        print('Bye Bye 謝謝惠顧')

if __name__ == '__main__':
    run()
        

