from lesson4 import *


def test_linear_search():
    assert linear_search([1, 5, 6, 4, 3, 2, 8], 4) == 3


def test_binery_search():
    assert binery_search(
        [3, 5, 7, 9, 11, 13, 15, 31, 100, 500, 600, 606, 701, 900], 31) == 7
