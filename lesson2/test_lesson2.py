from quiz import *


def test_even():
    assert even([1, 2, 3, 4, 5, 6, 7, 8, 12, 25, 26,
                 20]) == [2, 4, 6, 8, 12, 26, 20]


def test_fizzbuzz():
    assert fizzbuzz([1, 2, 3, 4, 5, 15, 30
                     ]) == [1, 2, 'fizz,', 4, 'buzz', 'fizzbuzz', 'fizzbuzz']


def test_vending_machine():
    assert vending_machine(269, 1000) == {500: 1, 100: 2, 10: 2, 1: 1}


def test_convert():
    assert convert(10, 2) == "1010"


def test_is_prime():
    assert is_prime(99) == False


def test_eratosthenes():
    assert eratosthenes(20) == [1, 2, 3, 5, 7, 11, 13, 17, 19]


def test_fibonacci():
    assert fibonacci(8) == 21


def test_leap_year():
    assert leap_year() == []


def test_japna_year():
    assert japan_year(2016)
