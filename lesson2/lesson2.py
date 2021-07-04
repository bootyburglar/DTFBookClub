from typing import List, Dict, AnyStr
from math import sqrt


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
    return [number for number in numbers if number % 2 == 0]


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
    #code here
    isDividBy3 = 'fizz'
    isDividBy5 = 'buzz'
    isDividBy3And5 = isDividBy3 + isDividBy5

    answer = []

    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            answer.append(isDividBy3And5)
        elif number % 3 == 0:
            answer.append(isDividBy3)
        elif number % 5 == 0:
            answer.append(isDividBy5)
        else:
            answer.append(number)
    return answer


def vending_machine(total: int, insert: int) -> Dict:
    """
    輸入total代表購買總價格 insert代表投入的錢 輸出找的錢 以dict來表示

    Args:
        total (int):購買總價格
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
    coins = [5000, 1000, 500, 100, 50, 10, 5, 1]
    change = {}
    total_change = insert - total
    for coin in coins:
        if total_change >= coin:
            coin_count, total_change = divmod(total_change, coin)
            change.update({coin: coin_count})
    return change


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
    while num > 0:
        num, leave = divmod(num, base)
        result = str(leave) + result
    return result


def is_prime(num: int) -> bool:
    """
    找出質數 是質數return True否則為False

    Args:
        num (int):輸入的數字

    Returns:
        boolean
    """
    if num <= 1: return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0: return False
    return True


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
    if num <= 1: return False
    prime = [2]
    limit = int(sqrt(num))
    data = [i for i in range(3, num, 2)]
    while limit >= data[0]:
        prime.append(data[0])
        data = [d for d in data if d % data[0] != 0]
    return prime + data


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
    fib = fibonacci_init_list
    for i in range(2, num):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[num - 1]


def leap_year() -> List:
    """
    找出1950到2050間的閏年
    能被4乘除的年份是閏年
    可以被100整除但不能被400整除的不是閏年

    Returns:
        list
    """
    def check_leap_year(year: int):
        if (year % 4 == 0):
            if ((year % 100 == 0) and year % 400 != 0):
                return False
            else:
                return True
        return False

    return [year for year in range(1950, 2050 + 1) if check_leap_year(year)]


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
    japan_year = {
        2019: "令和元年",
        1989: "平成元年",
        1926: "昭和元年",
        1912: "大正元年",
        1868: "明治元年",
    }
    for _year, name in japan_year.items():
        if year >= _year:
            year_count = year - _year
            if year_count:
                return name.replace('元', str(year - _year))
            return name
    else:
        return ''
