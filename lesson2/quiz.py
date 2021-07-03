from typing import List, Dict, AnyStr
"""
2.1 even
input: a list of numbers
output: return only the even numbers
"""


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
    #code here
    pass


"""
2.2 fizzbuzz
input: a list of numbers
output: print out fizz if divisible by 3
        print out fuzz if divisible by 5
        print out fizzbuzz if divisible by both 3 and 5
"""


def fizzbuzz(numbers: List) -> List:
    '''
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
    '''
    result = None
    #code here
    return result


"""
2.3 vending machine
input: an insert value and a product value
output: a dictionary of change and its numbers
"""


def vending_machine(product: int, insert: int) -> Dict:
    '''
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
    '''
    result = {}
    #code here
    return result


"""
2.4 convert
input: a value n and a base
output: the value in its specific base
"""


def convert(num: int, base: int) -> str:
    '''
    以base進位轉換num

    Args:
        num (int):被轉換的數字
        base (int):以多少進位

    Returns:
        int 轉換之後的數字

    Example:
        convert(20,2)
        > '1010'
    '''
    result = ''
    #code here
    return result


"""
2.5.1 is_prime
input: a number
output: True if the number is prime, False if not
"""


def is_prime(num: int) -> bool:
    '''
    找出質數 是質數return True否則為False

    Args:
        num (int):輸入的數字

    Returns:
        boolean
    '''
    ## code here
    return


"""
2.5.2 eratosthenes
input: a number n
output: a list of prime numbers smaller than n
"""


def eratosthenes(num: int) -> List:
    '''
    找出num範圍內的質數

    Args:
        num (int):輸入的數字範圍

    Returns:
        list

    Example:
        eratosthenes(10)
        > [1,2,3,5,7]
    '''
    #code here
    pass


"""
2.6 fibonacci
input: a number n
output: a list of fibonacci numbers smaller than n
"""


def fibonacci(num: int) -> int:
    '''
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
    '''
    fibonacci_init_list = [1, 1]
    #code here
    return


"""
quiz 1 leap year from 1950 to 2050
input: None
output: a leap year list
"""


def leap_year() -> List:
    '''
    找出1950到2050間的閏年
    能被4乘除的年份是閏年
    可以被100整除但不能被400整除的不是閏年

    Returns:
        list
    '''
    #code here
    return


"""
quiz 2 convert year to japan year
input: 1986 <= year <= 2020
output: japan year name
"""


def japan_year(year: int) -> str:
    '''
    輸入year西元年份 輸出日本年份
    明治元年1868 大正元年1912 昭和元年1926 平成元年1989 令和元年2019

    Args:
        year (int):西元年份

    Returns:
        str

    Examples:
        japan_year(2000))
        > 平成12年
    '''
    #code here
    return
