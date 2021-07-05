from typing import List, Dict, AnyStr


def even(numbers: List) -> List:
           
    """
    Args:
        numbers (list):一串數字

    Returns:
        list

    Example:
        even([1,2,3,4,5,6])
        > [2,4,6]
    """
    number_01=[]
    for a in numbers:
        if a %2 ==0:
           number_01.append(a)
        else:
           continue
    return number_01


def fizzbuzz(numbers: List) -> List:
    """
    輸入一串數字numbers
    3的倍數輸出fizz
    5的倍數輸出buzz
    3和5的倍數輸出fizzbuzz
    都不是的話輸出數字

    Args:
        num (int):要判斷的數字

    Returns:
        list

    Example:
        fizzbuzz([1,2,3,4,5,15])
        >[1,2,'fizz',4,'buzz','fizzbuzz']
    """
    number_02=[]
    for sum in numbers:
        if sum%3 ==0 and sum %5 ==0:
            number_02.append('fizzbuzz')  
        elif sum %3 ==0:
            number_02.append('fizz')
        elif sum %5 ==0:
            number_02.append('buzz')
        else :
            number_02.append(sum)
    return number_02


def vending_machine(product: int, insert: int) -> Dict:
    """
    輸入product代表購買總價格 insert代表投入的錢 輸出找的錢 以dict來表示

    Args:
        product (int):購買總價格
        insert (int):投入的錢

    Returns:
        dict 找的零錢 用5000 1000 500 100 50 10 5 1 為單位組成

    Example:
        vending_machine(4935,6000)
        > {
            1000:1,
            50:1,
            10:1
            5:1
        }
    """
    dollar={}
    dollar_total=insert-product
    
    r5000=dollar_total//5000  #餘數 
    q5000=dollar_total%5000   #商數
    dollar.update({5000:r5000})
    
    r1000=dollar_total//1000  #餘數 
    q1000=dollar_total%1000   #商數
    dollar.update({1000:r1000})
    
    r500=q1000//500  #餘數 
    q500=q1000%500   #商數
    dollar.update({500:r500})
   
    r100=q500//100  #餘數 
    q100=q500%100   #商數
    dollar.update({100:r100})

    r50=q100//50  #餘數 
    q50=q100 %50   #商數
    dollar.update({50:r50})

    r10=q50 //10  #餘數 
    q10=q50 %10   #商數
    dollar.update({10:r10})
   
    r5=q10//5  #餘數 
    q5=q10%5   #商數
    dollar.update({5:r5})
 
    r1=q5//1  #餘數 
    q1=q5%1   #商數
    dollar.update({1:r1})

    final_answer={}
    for key,value in dollar.items():
        if value != 0:
            final_answer.update({key:value})

    # 如何使用減的?
    # for key,value in dollar.items():
    #     if value ==0:
    # k=500
    # del dollar[]

    
    return final_answer


def convert(num: int, base: int) -> str:
    '''
    以base進位轉換num

    Args:
        num (int):被轉換的數字
        base (int):以多少進位

    Returns:
        int 轉換之後的數字

    Example:
        convert(10,2)
        > '1010'
    '''
    result = ''
    while num >0:
        result = str( num % base) + result
        num//= base

    return result


def is_prime(num: int) -> bool:
    """
    找出質數 是質數return True否則為False

    Args:
        num (int):輸入的數字

    Returns:
        boolean
    """
    if num//2==1:
        return(True)
    else:
        return(False)



def eratosthenes(num: int) -> List:
    """
    找出num範圍內的質數

    Args:
        num (int):輸入的數字範圍

    Returns:
        list

    Example:
        eratosthenes(10)
        > [1,2,3,5,7]
    """
 #未寫完
    export=[]
    for count in range(num):
        if num%2==1:
            export.append[num]
    return export


def fibonacci(num: int) -> int:
    """
    fibonacci 數列 前兩個數總和等於第三個
    1,1,2,3,5,8,13,21......
    數入num代表要輸出fibonacci數列裡面第幾個數字

    Args:
        num (int):fibonacci數列裡面第幾個數字

    Returns:
        int

    Example:
        fibonacci(5)
        > 5
        fibonacci(8)
        > 21
    """
    fibonacci_init_list = [1, 1]
    #code here
    pass


def leap_year() -> List:
    """
    找出1950到2050間的閏年
    能被4乘除的年份是閏年
    可以被100整除但不能被400整除的不是閏年

    Returns:
        list
    """
    #code here
    pass


def japan_year(year: int) -> str:
    """
    輸入year西元年份 輸出日本年份
    明治元年1868 大正元年1912 昭和元年1926 平成元年1989 令和元年2019

    Args:
        year (int):西元年份

    Returns:
        str

    Examples:
        japan_year(2000))
        > 平成12年
    """
    #code here
    pass
