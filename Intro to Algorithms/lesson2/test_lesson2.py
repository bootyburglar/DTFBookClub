from lesson2 import *


def test_even():
    assert even([1, 2, 3, 4, 5, 6, 7, 8, 12, 25, 26,
                 20]) == [2, 4, 6, 8, 12, 26, 20]


def test_fizzbuzz():
    assert fizzbuzz([1, 2, 3, 4, 5, 15,
                     30]) == [1, 2, 'fizz', 4, 'buzz', 'fizzbuzz', 'fizzbuzz']


def test_vending_machine():
    assert vending_machine(269, 1000) == {500: 1, 100: 2, 10: 3, 1: 1}


def test_convert():
    assert convert(10, 2) == "1010"


def test_is_prime():
    assert is_prime(99) == False


def test_eratosthenes():
    assert eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_fibonacci():
    assert fibonacci(8) == 21


def test_leap_year():
    assert leap_year() == [
        1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996,
        2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044,
        2048
    ]


def test_japna_year():
    assert japan_year(2000) == '平成12年'
